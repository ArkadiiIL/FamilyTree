from familytree.Family import FamilyTree
from collections import defaultdict
import time

all_family = defaultdict()
static_id = 0
static_current_family = None


def generate(family_name):
    global static_id
    static_id += 1
    family = FamilyTree(static_id, family_name)
    all_family[static_id] = family
    return family


def create_family():
    family_tree_name = str(input("Please enter your FamilyTree name: "))
    family_tree = generate(family_tree_name)
    global static_current_family
    static_current_family = family_tree
    time.sleep(1)
    print("You create {family_tree_name} family with id: {family_id} ".format(family_tree_name=family_tree_name,
                                                                              family_id=family_tree.get_id()))


def set_current_family(family):
    global static_current_family
    static_current_family = family


def get_current_family():
    return static_current_family
