import hmac
import hashlib
import base64
from backend.config.config import settings

SECRET_KEY = settings.SECRET_KEY.encode()

def generate_token(db: str, media_id: str) -> str:
    data = f"{db}:{media_id}".encode()
    signature = hmac.new(SECRET_KEY, data, hashlib.sha256).digest()
    token = base64.urlsafe_b64encode(data + b"::" + signature).decode()
    return token

def decode_token(token: str) -> tuple:
    try:
        raw = base64.urlsafe_b64decode(token.encode())
        data_part, sig_part = raw.rsplit(b"::", 1)
        expected_sig = hmac.new(SECRET_KEY, data_part, hashlib.sha256).digest()
        if not hmac.compare_digest(sig_part, expected_sig):
            raise ValueError("Invalid signature")
        db, media_id = data_part.decode().split(":")
        return db, media_id
    except Exception:
        raise ValueError("Invalid token")