import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # API keys and external service configurations
    OPENSUBTITLES_API_KEY = os.getenv('OPENSUBTITLES_API_KEY')
    OMDB_API_KEY = os.getenv('OMDB_API_KEY')
    TMDB_API_KEY = os.getenv('TMDB_API_KEY')
    
    # Application settings
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    
    # Model settings
    SUMMARIZATION_MODEL = os.getenv('SUMMARIZATION_MODEL', 'facebook/bart-large-cnn')
    MAX_INPUT_LENGTH = int(os.getenv('MAX_INPUT_LENGTH', 1024))
    
    # Other configurations can be added here as needed
