from unittest import TestCase
from profile import Profile
from unittest import TestCase

class TestProfile(TestCase):

    def setUp(self):
        self.__profile = Profile()
        self.__profile.set_user_name("user")
        self.__profile.set_type("hardware")

    def test_get_name(self):
        test_result = self.__profile.get_user_name()
        self.assertEqual(test_result, "user")

    def test_get_type(self):
        test_result = self.__profile.get_type()
        self.assertEqual(test_result, "hardware")