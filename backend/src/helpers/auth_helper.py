from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_database
from src.infra.providers import token_provider
from src.infra.sqlalchemy.repositories.user_repository import UserRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_user_logged(token: str = Depends(oauth2_scheme),
                    db: Session = Depends(get_database)):

    exception = HTTPException(status_code=401, detail="token inválido")

    try:
        phone = token_provider.verify_access_token(token)
    except JWTError:
        raise exception

    if not phone:
        raise exception

    user = UserRepository(db).list_by_phone(phone)
    if not user:
        raise exception

    return user
