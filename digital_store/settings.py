import os
from pathlib import Path
# 1. Turn off debug mode for safety on the internet
DEBUG = False

# 2. Allow any domain name to access your site
ALLOWED_HOSTS = ['*']

# 3. Add WhiteNoise to your MIDDLEWARE list (Put it right below SecurityMiddleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # <-- Add this line right here
    'django.contrib.sessions.middleware.SessionMiddleware',
    # ... keep all other lines the same
]

# 4. Add this static root directory setting at the very bottom
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
