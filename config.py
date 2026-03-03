
class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:1234@localhost:5432/hbomax_clone"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "super-secret-key"