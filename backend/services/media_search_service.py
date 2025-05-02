from typing import List
from backend.models.models import MediaItem
from backend.utils.security import generate_token

class MediaService:
    def __init__(self, media_repository):
        self.repo = media_repository

    def search(self, keyword: str = None, db_filter: List[str] = []) -> List[MediaItem]:
        results = self.repo.search_media(keyword, db_filter)
        items = []
        for hit in results.get("hits", {}).get("hits", []):
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
        return items
