class Fellow:
    def __init__(self, fname, track, familiars):
        self.fname = fname
        self.track = track
        self.familiars = familiars

    def __eq__(self, obj):
        return self.name == obj.name and self.track == obj.track

    def print_familiars(self):
        print("This fellow knows")
        for memb in self.familiars:
            print(memb)


# TODO: create "Gustavo", assign him to "DS", and give him an empty list
# for familiars
person1 = Fellow("Gustavo", "DS", ["Farukh", "Mo", "Tim"])

# TODO: print out his name using the 'person1' object
print(person1.fname)

# TODO: print out his track using the 'person1' object
print(person1.track)

# TODO: call the 'print_familiars()' method
person1.print_familiars()
