from backend.utils.security import generate_secure_token

class MediaURLBuilder:
    @staticmethod
    def build_secure_thumbnail_url(db: str, media_id: str) -> str:
        token = generate_secure_token(db, media_id)
        return f"/thumbnail/{db}/{media_id}?token={token}"

