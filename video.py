""" This is the entity, Video"""
from profile import Profile


class Video(Profile):

    def __init__(self):
        super().__init__()
        self.__time_limit = 10.0  # default minutes

    def get_time_limit(self):
        return self.__time_limit

    def set_time_limit(self, period):
        self.__time_limit = period
