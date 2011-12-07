import unittest
from django.conf import settings


"""
Subclass for field test cases
"""
class FieldTestCase(unittest.TestCase):

    def setUp(self):
        self.old_installed_apps = settings.INSTALLED_APPS
        settings.INSTALLED_APPS.append('django_extensions.tests')
        loading.cache.loaded = False
        migrate = True
        for app in settings.INSTALLED_APPS:
            if app == "south":
                migrate = False
        call_command('syncdb', verbosity=0, migrate=migrate)

    def tearDown(self):
        settings.INSTALLED_APPS = self.old_installed_apps
