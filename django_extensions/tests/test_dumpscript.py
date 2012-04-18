import sys
from field import FieldTestCase
from StringIO import StringIO
from django.test import TestCase
from django.core.management import call_command
from django_extensions.tests.models import Name

class DumpScriptTests(FieldTestCase):
    def setUp(self):
        super(DumpScriptTests, self).setUp()
        self.real_stdout = sys.stdout
        sys.stdout = StringIO()
        self.real_stderr = sys.stderr
        sys.stderr = StringIO()

    def tearDown(self):
        sys.stdout = self.real_stdout
        sys.stderr = self.real_stderr

    def test_runs(self):
        # lame test...does it run?
        n = Name(name='Gabriel')
        n.save()
        call_command('dumpscript', 'tests')
        self.assertTrue('Gabriel' in sys.stdout.getvalue())
