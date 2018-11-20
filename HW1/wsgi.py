import sys
from django.core.wsgi import get_wsgi_application

sys.path.append('/home/akondratjeva/nonsemiotic')
sys.path.append('/home/akondratjeva/nonsemiotic/lextyp')

application = get_wsgi_application()