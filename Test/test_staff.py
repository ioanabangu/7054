from contract import Contract
from profile import Profile
from unittest import TestCase
from staff import Staff

class TestStaff(TestCase):

    def setUp(self):
        self.__staff = Staff()
        self.__staff.set_user_name("user")
        self.__staff.set_email("user@gmail.com")
        self.__staff.set_start_year("2020")
        self.__staff.set_role("hardware")
        self.__profile = Profile()
        self.__contract = Contract()

    def test_get_name(self):
        test_result = self.__staff.get_user_name()
        self.assertEqual(test_result, "user")


    def test_get_email(self):
        test_result = self.__staff.get_email()
        self.assertEqual(test_result, "user@gmail.com")

        def test_get_start_year(self):
            test_result = self.__staff.get_start_year()
            self.assertEqual(test_result, "2020")