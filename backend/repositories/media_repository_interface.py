from abc import ABC, abstractmethod
from typing import List
from backend.models.models import MediaSearchResponse

class MediaRepository(ABC):
    @abstractmethod
    def search_media(self, keyword: str = None, db_filter: List[str] = []) -> MediaSearchResponse:
        pass
