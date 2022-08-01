class Config:
    TESTING = False
    SECRET_KEY = "secretashella"
    SQLACHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev-db.sqlite"

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev-db.sqlite"

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev-db.sqlite"

