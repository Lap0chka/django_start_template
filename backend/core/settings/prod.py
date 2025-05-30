from base import *  # noqa: F401
from .logger_config import LOGGING  # noqa: F401


ALLOWED_HOSTS = []

# Cors

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "http://localhost:3000",
]

# Secure

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'  # или SAMEORIGIN
SECURE_HSTS_SECONDS = 31536000  # включить при HTTPS
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = True  # перенаправлять с HTTP на HTTPS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# CSP

MIDDLEWARE += ['csp.middleware.CSPMiddleware']

CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'", "https://trusted.cdn.com")