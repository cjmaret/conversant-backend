import os
from dotenv import load_dotenv

if os.path.exists(".env.development"):
    load_dotenv(dotenv_path=".env.development")

class Config:
    ENV = os.getenv("ENV", "production")
    MONGO_URI = os.getenv("MONGO_URI")
    TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM", "HS256")
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
    GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI")

    @staticmethod
    def validate():
        required_vars = ["TOGETHER_API_KEY", "SECRET_KEY",
                         "GOOGLE_CLIENT_ID", "GOOGLE_REDIRECT_URI"]
        for var in required_vars:
            if not getattr(Config, var):
                raise EnvironmentError(
                    f"Missing required environment variable: {var}")
