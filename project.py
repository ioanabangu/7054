""" This is the entity, Project"""


class Project:

    def __init__(self):  # a method to create objects
        self.__name = "user"  # private attribute

    def get_name(self):  # get method
        return self.__name

    def set_name(self, team):  # set method
        self.__name = team



