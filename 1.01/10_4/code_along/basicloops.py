participants = 0
heard = 0

while True:
    if participants == 10:
	    break

    ans = input("Have you ever heard of fruit loops?")
    if ans == "no":
	    continue
    elif ans == "yes":
	    heard += 1
        participants += 1