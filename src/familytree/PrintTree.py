def print_tree(person):
    ancestors = []
    fill_ancestors(ancestors, person)
    for ancestor in ancestors:
        print_person(ancestor)


def fill_ancestors(ancestors, person):
    ancestors.append(person)
    if person.get_father() is not None:
        fill_ancestors(ancestors, person.get_father())
    if person.get_mother() is not None:
        fill_ancestors(ancestors, person.get_mother())


def print_person(person):
    sex = None
    if person.get_person_sex():
        sex = "son"
    else:
        sex = "daughter"
    first_string = "I am {person_name} {person_surname}".format(person_name=person.get_person_name(),
                                                                person_surname=person.get_person_surname())
    if person.get_father() is not None or person.get_mother() is not None:
        first_string += " the {sex} of ".format(sex=sex)
        if person.get_father() is not None and person.get_mother() is None:
            first_string += person.get_father().get_person_name() + " " + person.get_father().get_person_surname()
        elif person.get_father() is None and person.get_mother() is not None:
            first_string += person.get_mother().get_person_name() + " " + person.get_mother().get_person_surname()
        else:
            first_string += person.get_father().get_person_name() + " " + person.get_father().get_person_surname() + \
                            " and " + person.get_mother().get_person_name() + \
                            " " + person.get_mother().get_person_surname()
    print(first_string)
