""" This is the entity, Text"""
from profile import Profile


class Text(Profile):

    def __init__(self):
        super().__init__()
        self.__word_limit = 1000  # default

    def get_word_limit(self):
        return self.__word_limit

    def set_word_limit(self, limit):
        self.__word_limit = limit



