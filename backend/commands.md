## commands

    - pipenv install fastapi[all]
    - pipenv install sqlalchemy

    run server
    - uvicorn name_file:app --reload
    - uvicorn src.server:app --reload --reload-dir=src

## instalar gerenciador de migrations
    - pipenv install alembic
    - na raiz do projeto rode: alembic init alembic
    - abra o arquivo env.py e import o Base do SQLAlchemy
        - from src.infra.sqlalchemy.config.database import Base
        - from src.infra.sqlalchemy.models.models import *
        - target_metadata = Base.metadata
    - informe a URL do banco de dados no arquivo (alembic.ini)
        - sqlalchemy.url == url do banco
    - executar migration
        - alembic revision --autogenerate -m "commit"
        - alembic upgrade head

## hash password
    - pipenv install passlib[bcrypt]

## JWT 

    - pipenv install python-jose[cryptography]

        