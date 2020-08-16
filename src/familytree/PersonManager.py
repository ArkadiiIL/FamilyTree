from collections import defaultdict
import time

from familytree.Person import Person


class PersonGenerator:
    def __init__(self):
        self.__all_persons = defaultdict()
        self.__static_current_person = None
        self.__static_person_id = 0

    def create_person(self):
        time.sleep(1)
        name = str(input("Please enter name "))
        surname = str(input("Please enter surname "))
        sex = str(input("Please enter sex male/female "))
        self.__static_person_id += 1
        if sex == "female":
            sex = False
        else:
            sex = True
        person = Person(self.__static_person_id, name, surname, sex)
        self.__all_persons[self.__static_person_id] = person
        self.__static_current_person = person

    def get_current_person(self):
        return self.__static_current_person

    def set_current_person(self, person_id):
        self.__static_current_person = self.__all_persons[person_id]

    def get_all_persons(self):
        return self.__all_persons

    def delete_person(self, person_id):
        self.__all_persons.pop(person_id)
        return len(self.__all_persons)
