from .base import *
from .utils import read_or_get

DEBUG = False
ALLOWED_HOSTS = ['*']

SECRET_KEY = read_or_get('/private/secrets', 'SECRET_KEY', None)
