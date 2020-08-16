from collections import defaultdict

from familytree.PersonManager import PersonGenerator


class FamilyTree:

    def __init__(self, family_id, name):
        self.__id = family_id
        self.__name = name
        self.__family_members = defaultdict()
        self.__person_generator = PersonGenerator()

    def get_name(self):
        return self.__name

    def set_person(self, person):
        self[person.id] = person

    def get_person(self, person_id):
        return self.__family_members[person_id]

    def get_id(self):
        return self.__id

    def get_person_generator(self):
        return self.__person_generator
