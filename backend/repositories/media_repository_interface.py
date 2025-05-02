from abc import ABC, abstractmethod
from typing import Any, List

class BaseMediaRepository(ABC):
    @abstractmethod
    def search_media(self, keyword: str = None, db_filter: List[str] = []) -> Any:
        pass
