# Create your tests here.
import datetime

from django.contrib.auth.models import User
from user_profiles.models import Profile
from django.test.testcases import TestCase


class TestUserProfiles(TestCase):

    def setUp(self) -> None:

        self.test_user1 = User.objects.create_user(username='test_user1',
                                                   email='testuser1@testuser.com',
                                                   password='UserPass1')
        self.test_user1.save()

        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

