import time
from familytree.FamilyManager import all_family, create_family, set_current_family, get_current_family
from familytree.PrintTree import print_tree


def main_menu():
    print("Please select further command")
    time.sleep(1)
    print("1.Create Family")
    print("2.Get all family")
    print("Or something else for exit!")
    answer = str(input())
    if answer == "1":
        create_family()
        family_menu()
    elif answer == "2":
        get_all_family_menu()
    else:
        time.sleep(1)
        print("Bye bye!")


def family_menu():
    print("Your family now is {family_name} with id: {family_id} \n Please select further command"
        .format(
        family_name=get_current_family().get_name(),
        family_id=get_current_family().get_id()))

    time.sleep(1)
    print("1.Get person menu")
    print("2.Create new family")
    print("3.Return to main menu")
    print("Or something else for exit!")
    answer = str(input())
    time.sleep(1)
    if answer == "1":
        person_menu()
    elif answer == "2":
        create_family()
        family_menu()
    elif answer == "3":
        main_menu()
    else:
        time.sleep(1)
        print("Bye bye!")


def get_all_family_menu():
    if len(all_family) > 0:
        print_all_family()
        print("Please select further command")
        time.sleep(1)
        print("1.Choose family")
        print("2.Delete family")
        print("Or something else for exit!")
        answer = str(input())
        time.sleep(1)
        if answer == "1":
            number_family = int(input("Please enter family id: "))
            set_current_family(all_family[number_family])
            family_menu()
        elif answer == "2":
            number_family = int(input("Please enter family id: "))
            all_family.pop(number_family)
            if len(all_family) <= 0:
                print("You haven't family, please create family")
                create_family()
            elif number_family == get_current_family().get_id:
                print_all_family()
                current = int(input("Please enter new current family id: "))
                set_current_family(all_family[current])
                family_menu()
            else:
                family_menu()
        else:
            time.sleep(1)
            print("Bye bye!")
    else:
        print("Your didn't create family")
        main_menu()


def person_menu():
    person_generator = get_current_family().get_person_generator()
    time.sleep(1)
    if person_generator.get_current_person() is None:
        print("You haven't person in {family_name} family".format(family_name=get_current_family().get_name()))
        print("Please select further command")
        time.sleep(1)
        print("1.Create Person")
        print("2.Return to family menu")
        print("Or something else for exit!")
        answer = str(input())
        if answer == "1":
            person_generator.create_person()
            person_menu()
        elif answer == "2":
            family_menu()
        else:
            time.sleep(1)
        print("Bye bye!")
    else:
        print("Your current person now is {person_name} {person_surname} with id: {person_id} \n Please select further command"
            .format(
            person_name=person_generator.get_current_person().get_person_name(),
            person_surname=person_generator.get_current_person().get_person_surname(),
            person_id=person_generator.get_current_person().get_person_id()))

    time.sleep(1)
    print("1.Create new Person")
    print("2.Change current person")
    print("3.Delete person")
    print("4.Add father")
    print("5.Add mother")
    print("6.Add child")
    print("7.Print Tree")
    print("8.Return to family menu")
    print("Or something else for exit!")
    answer = str(input())
    time.sleep(1)
    if answer == "1":
        person_generator.create_person()
        person_menu()
    elif answer == "2":
        print_all_person()
        number_person = int(input("Please enter person id: "))
        person_generator.set_current_person(number_person)
        person_menu()
    elif answer == "3":
        print_all_person()
        number_person = int(input("Please enter person id: "))
        length = person_generator.delete_person(number_person)
        if length <= 0:
            person_generator.set_current_person(None)
            person_menu()
        elif number_person == person_generator.get_current_person():
            print("Please select new current person")
            print_all_person()
            current_person = int(input("Please enter person id: "))
            person_generator.set_current_person(current_person)
            person_menu()
    elif answer == "4":
        print_all_person()
        number_person = int(input("Please enter person id: "))
        if number_person == person_generator.get_current_person().get_person_id():
            print("Please select not current person")
            person_menu()
        else:
            person_generator.get_current_person().set_father(person_generator.get_all_persons()[number_person])
            person_menu()
    elif answer == "5":
        print_all_person()
        number_person = int(input("Please enter person id: "))
        if number_person == person_generator.get_current_person().get_person_id():
            print("Please select not current person")
            person_menu()
        else:
            person_generator.get_current_person().set_mother(person_generator.get_all_persons()[number_person])
            person_menu()
    elif answer == "6":
        print_all_person()
        number_person = int(input("Please enter person id: "))
        if number_person == person_generator.get_current_person().get_person_id():
            print("Please select not current person")
            person_menu()
        else:
            person_generator.get_current_person().set_child(person_generator.get_all_persons()[number_person])
            person_menu()
    elif answer == "7":
        print_tree(person_generator.get_current_person())
        person_menu()
    elif answer == "8":
        family_menu()
    else:
        time.sleep(1)
        print("Bye bye!")


def print_all_family():
    for family_id in all_family:
        family = all_family[family_id]
        print("{family_id}. {family_name}".format(family_id=family.get_id(),
                                                  family_name=family.get_name()))


def print_all_person():
    all_person = get_current_family().get_person_generator().get_all_persons()
    for person_id in all_person:
        person = all_person[person_id]
        print("{person_id}. {name} {surname}".format(person_id=person.get_person_id(),
                                                     name=person.get_person_name(),
                                                     surname=person.get_person_surname()))
