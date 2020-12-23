from django.test import TestCase
from .models import Profile,Posts,Comments,Following

# Testing the 'Following' and 'Comments'

class FollowingTestClass(TestCase):
    def setUp(self):
        self.esther=Following(username='mykey',followed='marabel')
                            
    def test_instance(self):
        self.assertTrue(isinstance(self.mykey,Following))

class CommentTestClass(TestCase):
    def setUp(self):
        self.first=Comment(post=1,
                            username='mykey',
                            comment='What a great throw-back',
                            date='Jan 07, 2020, 08:50 a.m.',
                            count=0)

    def test_instance(self):
        self.assertTrue(isinstance(self.first,Comment))