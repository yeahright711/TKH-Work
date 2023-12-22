from Person import PersonClass


# TODO: implement Fellow class that inherits from "Person"
# we just include another method called "form_group()"
# that prints out all the people that this fellow knows
# using a for-loop. Implement below

class Fellow(PersonClass):
    def form_group(self):
        for fname in self.people:
            print(fname)

fellowA = Fellow("Farukh", "Hummus", ["Mo","Tim", "Caridad"])


fellowA.form_group() 