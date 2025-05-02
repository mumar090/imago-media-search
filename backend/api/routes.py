from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
from backend.config.config import settings
from backend.models.models import MediaSearchRequest, MediaSearchResponse
from backend.services.media_search_service import MediaService
from backend.repositories.elastic_media_repository import ElasticsearchRepository
from backend.utils.security import generate_token, decode_token

router = APIRouter()

search_service = MediaService(ElasticsearchRepository())

@router.get("/")
def root():
    return {"message": "IMAGO Media Search API"}

@router.post("/search", response_model=MediaSearchResponse)
def search_media(request: MediaSearchRequest):
    try:
        documents = search_service.search(keyword=request.keyword, db_filter=request.db_filter)
        for doc in documents:
            doc.thumbnail_url = f"/thumbnail/{generate_token(doc.db, doc.media_id)}"
        return MediaSearchResponse(results=documents)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/thumbnail/{token}")
def serve_thumbnail(token: str):
    try:
        db, media_id = decode_token(token)
    except ValueError:
        raise HTTPException(status_code=403, detail="Invalid token")

    padded_id = str(media_id).zfill(10)
    full_url = f"{settings.BASE_URL}/{db}/{padded_id}/s.jpg"
    return RedirectResponse(url=full_url)