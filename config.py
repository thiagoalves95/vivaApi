import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'chavesecretateste290125'
    GROQ_API_KEY = os.environ.get('GROQ_API_KEY') or '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'
    GROQ_API_URL = 'https://api.groq.com/openai/v1/chat/completions'