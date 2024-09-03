import unittest
from project import Project

class TestProject(unittest.TestCase):

    def setUp(self):
        self.__project = Project()
        self.__project.set_name("user")


    def test_get_name(self):
        someresult = self.__project.get_name()
        # test_result = self.__project.get_name()
        self.assertEqual(someresult, "user")


if __name__ == '__main__':
    unittest.main()