import time

def giveTime():
    return time.time()


def makeSlides():
    print("Making slides...")
    time.sleep(2)
    print("DONE!")


class PersonClass:
    def __init__(self, name, food, people):
        self.name = name
        self.food = food
        self.people = people
  
    def fav_food(self):
        print(self.name, "likes", self.food)

# if you're wondering, what is this?
# try removing this conditional and running `Collaborator.py`
# see what happens!
if __name__ == "__main__":
    personA = PersonClass("Farukh", "Hummus", ["Mo", "Tim"])
    personA.fav_food()
