from django.test import TestCase

# Create your tests here.
from twitter.models import Tweet

class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Tweet.objects.create(name='Big Mama', tweet='The tweet for unity test')
