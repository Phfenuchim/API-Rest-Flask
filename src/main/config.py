import os

class Config:
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES", 2592000))  # 30days 
    JWT_TOKEN_LOCATION = ["headers", "cookies", "json", "query_string"]
    JWT_COOKIE_SECURE = True
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,
        "pool_recycle": 1800,  # 30 minutes
        "pool_size": 10,
        "max_overflow": 20,
    }
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    # print(os.getenv("JWT_SECRET_KEY"))
    # print(int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES", 2592000)) )
    # print(JWT_TOKEN_LOCATION)
    # print(os.getenv("JWT_COOKIE_SECURE"))
    # print(SQLALCHEMY_ENGINE_OPTIONS)
    # print(os.getenv("SQLALCHEMY_DATABASE_URI"))
    