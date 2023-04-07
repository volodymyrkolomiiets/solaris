import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Config:
    SECRET_KEY = 'iDxaR5EXFO8IdMrWjOKTPQ'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://main_user:main_pass@0.0.0.0:3306/user_db"
    SQLALCHEMY_ECHO=True


class ProductionConfig(Config):
    pass
