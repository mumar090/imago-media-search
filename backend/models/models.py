from typing import List, Optional
from pydantic import BaseModel

class MediaSearchRequest(BaseModel):
    keyword: Optional[str] = None
    db_filter: Optional[List[str]] = []

class MediaItem(BaseModel):
    media_id: str
    title: Optional[str] = None
    description: Optional[str] = None
    db: str
    thumbnail_url: str

class MediaSearchResponse(BaseModel):
    results: List[MediaItem]
