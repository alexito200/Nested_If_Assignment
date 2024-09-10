# Task 1 Code Correction

place = input("Choose a place: forest or cave? ")

if place == "forest": # I added another = because there was only one
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree": # I added another = because there was only one
        print("You found a bird's nest!")
    elif action == "cross a river": # I added another = because there was only one / also I changed the else to an elif
        print("You found a boat!")

# Task 2 Setting the Scene

elif place == "cave": # I added another = because there was only one
    action = input("light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("Go with the light!")
    elif action == "proceed in the dark":
        print("Good luck in the dark!")

# Task 3 Deafult Path

else:
    pass