import os
import sys

# Add your project directory to the sys.path
path = '/home/Hoopessentials/sportsessentials'
if path not in sys.path:
    sys.path.insert(0, path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sportsessentials.settings')

application = get_wsgi_application()