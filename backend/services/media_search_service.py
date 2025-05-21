#from typing import List
from backend.models.models import MediaSearchRequest, MediaItem, MediaSearchResponse
from backend.utils.security import generate_token
from backend.repositories.media_repository import ElasticsearchRepository

class MediaService:
    def __init__(self, media_repository:ElasticsearchRepository):
        self.repo = media_repository

    def search(self, request:MediaSearchRequest) -> MediaSearchResponse:
        results = self.repo.search_media(request.keyword, request.db_filter)
        hits = results.get("hits", {}).get("hits", [])
        items = []
        for hit in hits:
            src = hit.get("_source", {})
            media_id = src.get("bildnummer")
            db = src.get("db")

            if not media_id or not db:
                continue  # Skip invalid entries

            token = generate_token(db, media_id)
            thumb_url = f"/thumbnail/{token}"

            items.append(MediaItem(
                media_id=media_id,
                db=db,
                title=src.get("fotografen"),
                description=src.get("suchtext"),
                thumbnail_url=thumb_url
            ))

        return MediaSearchResponse(results=items)
