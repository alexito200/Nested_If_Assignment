# Task 1 Code Correction

attendees = int(input("Enter number of attendees: ")) # I added an int() function to convert user input into a whole number
entertainment = input("Tell me if you would like a band or a DJ: ") if attendees > 100 else "pass"
veggie_food = input("Would you like vegetarian food (yes/no):\n")

if attendees > 100:
    print("You will be placed into our Large Hall")
# Task 3 Catering Choices
    if veggie_food == "yes":
        print("Veggie Delight Caterers will cater your event")
    else:
        print("Gourmet Meals Caterers will cater your event.")
# Task 2 Venue Selection
    if entertainment == "band":
        print("The band will bring in their own audio system")
    elif entertainment == "DJ":
        print("We'll set up a nice audio system for the DJ")
else:
    print("You will be placed in our conference room")
    print("There is not enough room for entertainment")
    if veggie_food == "yes":
        print("Veggie Delight Caterers will cater your event.")
    else:
        print("Gourmet Meals Caterers will cater your event")