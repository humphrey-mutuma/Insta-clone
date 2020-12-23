from django.test import TestCase
from .models import Profile,Posts,Comments,Following

# Testing the 'Following' and 'Comments'

class FollowingTestClass(TestCase):
    def setUp(self):
        self.esther=Following(username='humphrey',followed='obama')
                            
    def test_instance(self):
        self.assertTrue(isinstance(self.mykey,Following))

class CommentTestClass(TestCase):
    def setUp(self):
        self.first=Comment(post=1,
                            username='humphrey',
                            comment='What a great coding challenge',
                            date='sep 07, 2020, 08:50 a.m.',
                            count=0)

    def test_instance(self):
        self.assertTrue(isinstance(self.first,Comment))