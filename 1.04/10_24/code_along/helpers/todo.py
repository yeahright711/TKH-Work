
def get_todo():
    with open("10_24/code_along/data/todo.txt") as f:
        lines = f.readlines()

        for row in lines:
            print(row)

get_todo()

print("youve ran todo.py")
