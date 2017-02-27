from .base import *


DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATE_CHOICES = [
    ('Bihar','Bihar')
]

try:
    from .local import *
except ImportError:
    pass
