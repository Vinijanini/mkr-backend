
class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:1@localhost:5432/mkr"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "super-secret-key"
