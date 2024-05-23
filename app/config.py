import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'you-will-never-guess')
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')