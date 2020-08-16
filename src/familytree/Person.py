from collections import defaultdict


class Person:

    def __init__(self, person_id, name, surname, sex, date_birth="unknown"):
        self.__person_id = person_id
        self.__name = name
        self.__surname = surname
        self.__sex = sex
        self.__status_life = True
        self.__date_birth = date_birth
        self.__date_death = None
        self.__children = None
        self.__spouse = None
        self.__father = None
        self.__mother = None

    def get_person_id(self):
        return self.__person_id

    def get_person_name(self):
        return self.__name

    def get_person_surname(self):
        return self.__surname

    def get_person_sex(self):
        return self.__sex

    def set_date_death(self, date):
        self.__date_death = date
        self.__status_life = False

    def get_status_life(self):
        return self.__status_life

    def set_father(self, father):
        self.__father = father

    def get_father(self):
        return self.__father

    def set_mother(self, mother):
        self.__mother = mother

    def get_mother(self):
        return self.__mother

    def set_spouse(self, spouse):
        self.__spouse = spouse

    def get_spouse(self):
        return self.__spouse

    def set_child(self, child):
        self.__children = defaultdict()
        self.__children[child.get_person_id()] = child

    def get_child(self, child_id):
        return self.__children[child_id]