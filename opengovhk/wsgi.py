import os
import sys
from django.core.wsgi import get_wsgi_application
from dj_static import Cling

# Calculate the path based on the location of the WSGI script.
apache_configuration = os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.join(project, '..')
sys.path.append(project)
sys.path.append(workspace)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'opengovhk.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Production')

# from configurations.wsgi import get_wsgi_application
# application = get_wsgi_application()

try:
    from dj_static import Cling
    # application = Cling(application)
	application = Cling(get_wsgi_application())
except ImportError:
    pass


