import unittest
from field import FieldTestCase

from django.db import connection
from django.conf import settings
from django.core.management import call_command
from django.db.models import loading
from django.db import models
from django_extensions.db.fields import UUIDField


class TestModel_field(models.Model):
    a = models.IntegerField()
    uuid_field = UUIDField()

class TestModel_pk(models.Model):
    uuid_field = UUIDField(primary_key=True)

class TestAgregateModel(TestModel_pk):
    a = models.IntegerField()

class TestManyToManyModel(TestModel_pk):
    many = models.ManyToManyField(TestModel_field)

class UUIDFieldTest(FieldTestCase):

    def testUUIDFieldCreate(self):
        j = TestModel_field.objects.create(a=6, uuid_field=u'550e8400-e29b-41d4-a716-446655440000')
        self.assertEquals(j.uuid_field, u'550e8400-e29b-41d4-a716-446655440000')

    def testUUIDField_pkCreate(self):
        j = TestModel_pk.objects.create(uuid_field=u'550e8400-e29b-41d4-a716-446655440000')
        self.assertEquals(j.uuid_field, u'550e8400-e29b-41d4-a716-446655440000')
        self.assertEquals(j.pk, u'550e8400-e29b-41d4-a716-446655440000')

    def testUUIDField_pkAgregateCreate(self):
        j = TestAgregateModel.objects.create(a=6)

    def testUUIDFieldManyToManyCreate(self):
        j = TestManyToManyModel.objects.create(uuid_field=u'550e8400-e29b-41d4-a716-446655440010')
        self.assertEquals(j.uuid_field, u'550e8400-e29b-41d4-a716-446655440010')
        self.assertEquals(j.pk, u'550e8400-e29b-41d4-a716-446655440010')

