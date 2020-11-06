from django.test import TestCase
from .models import Person

# Create your tests here.


class PersonTests(TestCase):
    def setUp(self):
        Person(name="foo").save()
        Person(name="bar").save()
        Person().save()

    def test_check_count(self):
        self.assertEqual(3, Person.objects.count())

    def test_check_contains(self):
        self.assertEqual(1, Person.objects.all().filter(name="foo").count())
