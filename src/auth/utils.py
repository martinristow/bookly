import jwt
from passlib.context import CryptContext
from datetime import timedelta, datetime, timezone
from src.config import settings
import uuid
from jwt.exceptions import PyJWTError
import logging

passwd_context = CryptContext(
    schemes=["bcrypt"]
)

ACCESS_TOKEN_EXPIRE = 3600


def generate_passwd_hash(password: str) -> str:
    password_hash = passwd_context.hash(password)

    return password_hash


def verify_password(password_plain: str, hash_pass: str) -> bool:
    return passwd_context.verify(password_plain, hash_pass)


def create_access_token(user_data: dict, expiry: timedelta = None, refresh: bool = False):
    expire_time = datetime.utcnow() + (expiry if expiry is not None else timedelta(seconds=ACCESS_TOKEN_EXPIRE))

    payload = {
        'user': user_data,
        'expire': int(expire_time.timestamp()),
        'jti': str(uuid.uuid4()),
        'refresh': refresh
    }

    token = jwt.encode(
        payload=payload,
        key=settings.JWT_SECRET,
        algorithm=settings.JWT_ALGORITHM
    )

    return token


def decode_token(token: str) -> dict:
    try:
        token_data = jwt.decode(
            jwt=token,
            key=settings.JWT_SECRET,
            algorithms=[settings.JWT_ALGORITHM]
        )

        return token_data

    except PyJWTError as e:
        logging.exception(e)
        return None

