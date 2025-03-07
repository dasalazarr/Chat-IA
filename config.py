"""
Configuration settings for the Chat IA application.
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Flask Configuration
SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
PORT = int(os.getenv('PORT', 5000))

# AI Model Configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4')

ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
ANTHROPIC_MODEL = os.getenv('ANTHROPIC_MODEL', 'claude-3-opus-20240229')

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
GOOGLE_MODEL = os.getenv('GOOGLE_MODEL', 'gemini-pro')

# Router Configuration
DEFAULT_MODEL = os.getenv('DEFAULT_MODEL', 'openai')  # Which model to use if routing can't decide
USE_MULTI_MODEL = os.getenv('USE_MULTI_MODEL', 'True').lower() == 'true'  # Whether to use multiple models

# Response Mixer Configuration
MIXER_STRATEGY = os.getenv('MIXER_STRATEGY', 'best_parts')  # Options: 'best_parts', 'average', 'vote'