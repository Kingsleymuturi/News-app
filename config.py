import os
from instance.config import API_KEY

class Config:
    API_KEY = API_KEY
    NEWS_API_BASE_URL='https://newsapi.org/v2/sources?country=us&category={}&apiKey={}'
    NEWS_ARTICLES_APL_URL='https://newsapi.org/v2/everything?q={}&apiKey={}'
    SOURCE_ARTICLES_URL='https://newsapi.org/v2/everything?sources={}&apiKey={}'

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig }