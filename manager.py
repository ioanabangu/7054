""" This is the entity, Manager"""
from staff import Staff
from contract import Contract

class Manager(Staff):

    def __init__(self):
        super().__init__()
        self.__bonus = 0.0
        self.__contract = Contract()

    def get_bonus(self):
        return self.__bonus

    def set_bonus(self, amount):
        self.__bonus = amount

    def get_contract(self):
        return self.__contract

    def get_total_pay(self):
        pay = self.get_contract.get_pay()  # contract payment
        total = pay + self.__bonus  # bonus
        return total


