import time

from familytree.FamilyManager import create_family
from familytree.MenuManager import family_menu


def main():
    time.sleep(2)
    print("Hello to FamilyTree builder")
    time.sleep(2)
    answer = str(input("If you want to create a tree please enter YES or enter something else for exit: "))
    if answer.lower() == "yes":
        create_family()
        family_menu()
    else:
        time.sleep(1)
        print("Bye bye!")


main()
