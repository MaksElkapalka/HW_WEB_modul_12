class Config:
    DB_URL = "postgresql+asyncpg://postgres:567234@localhost:5432/postgres"


config = Config


class Hash:
    KEY = "b9c25eac976d0331dbf0415b12f8e7c45ff7406a7fc842d53f221508b22ae95b"
    ALGORITHM = "HS256"


hashing = Hash


"""
docker run --name db-postgres -p 5432:5432 -e POSTGRES_PASSWORD=567234 -d postgres

"""
