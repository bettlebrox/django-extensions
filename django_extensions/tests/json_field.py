import unittest
from field import FieldTestCase

from django.db import connection
from django.conf import settings
from django.core.management import call_command
from django.db.models import loading
from django.db import models
from django_extensions.db.fields.json import JSONField


class TestModel(models.Model):
    a = models.IntegerField()
    j_field = JSONField()

class JsonFieldTest(FieldTestCase):

    def testCharFieldCreate(self):

        j = TestModel.objects.create(a=6, j_field=dict(foo='bar'))
        
