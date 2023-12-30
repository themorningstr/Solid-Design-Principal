# DIP :- Dependency Inversion Principal

from enum import Enum
from abc import abstractmethod

class Relationship(Enum):
    PARENT = 1
    CHILD = 2
    SIBLING = 3



class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        pass



class Relationships(RelationshipBrowser): #low level module
    def __init__(self):
        self.relations = []

    
    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
    
    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == "jhon" and r[1] == Relationship.PARENT:
                yield r[2].name



class Research:  #high level module
    def __init__(self, browser):
        for p in browser.find_all_children_of("jhon"):
            print(f"jhon has a child called {p}")

        



parent = Person("jhon")
child1 = Person("chris")
child2 = Person("matt")

