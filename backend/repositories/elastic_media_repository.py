from elasticsearch import Elasticsearch, BadRequestError, AuthenticationException, TransportError
from fastapi import HTTPException
from typing import List
import logging, urllib3

from backend.config.config import settings
from backend.repositories.media_repository_interface import BaseMediaRepository

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logger = logging.getLogger(__name__)

class ElasticsearchRepository(BaseMediaRepository):
    def __init__(self):
        try:
            self.client = Elasticsearch(
                settings.ES_HOST,
                basic_auth=(settings.ES_USER, settings.ES_PASSWORD),
                verify_certs=settings.VERIFY_CERTS
            )
            if not self.client.ping():
                raise ConnectionError("Could not connect to Elasticsearch cluster.")
        except AuthenticationException as e:
            logger.error(f"Elasticsearch authentication failed: {e}")
            raise HTTPException(status_code=401, detail="Invalid Elasticsearch credentials.")
        except Exception as e:
            logger.error(f"Elasticsearch connection error: {e}")
            raise HTTPException(status_code=500, detail="Failed to connect to Elasticsearch.")

        self.index = settings.ES_INDEX

    def search_media(self, keyword: str = None, db_filter: List[str] = []):
        query = {"bool": {"must": []}}

        if keyword:
            query["bool"]["must"].append({
                "multi_match": {
                    "query": keyword,
                    "fields": ["suchtext^2", "fotografen"]
                }
            })
        if db_filter:
            query["bool"]["filter"] = [{"terms": {"db": db_filter}}]

        logger.debug(f"Elasticsearch query: {query}")

        try:
            return self.client.search(index=self.index, body={"query": query})
        except AuthenticationException as e:
            logger.error(f"Authentication error while querying Elasticsearch: {e}")
            raise HTTPException(status_code=401, detail="Authentication failed while querying Elasticsearch.")
        except BadRequestError as e:
            logger.warning(f"Bad request to Elasticsearch: {e}")
            raise HTTPException(status_code=400, detail="Invalid search query.")
        except TransportError as e:
            logger.error(f"Transport error with Elasticsearch: {e}")
            raise HTTPException(status_code=503, detail="Elasticsearch service temporarily unavailable.")
        except Exception as e:
            logger.exception(f"Unexpected error querying Elasticsearch: {e}")
            raise HTTPException(status_code=500, detail="Unexpected server error during search.")