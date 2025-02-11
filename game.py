'''
DOCSTRING
adventure game 
author = utsav
'''
# Welcome message and introduction
print("welcome to the adventure game")

player_name = input("What is your name adventurer??: ")


# concatination of string 
print("welcome, " + player_name +  "!Your journey begins here now.")

#Using f-strings
print(f" welcome {player_name} Now you are in a long journey")



#Describe the starting area

Starting_area = """
You find yourslef in a dark forest
The sound of rustling leaves fills the air
A faint path lies ahead, leading deeper into the 
Unknown.....
"""
print(Starting_area)

#starting the loop
while True:
    print("\nYou see two path ahead: ")
    print("\t1. Take the left path into the dark woods.")
    print("\t2. Take the right path towards the mountain pass:")
    print("\t3. stay where you are.")

    decision = input("what will you do(1,2,3): ")

    if decision == "1":
        print(f"{player_name}, you step into the dark woods.\n The trees whisper as you walk deeper.")

    elif decision == "2":
        print(f" {player_name}, you make your way \n towards the mountain pass, feeling\n the cold wind against your face.")

    elif decision == "3":
        print("you stay still, listening to the\n distant sounds of the forest")

    
    else:
        print("Invalid Choice!, Please choose 1, 2 or 3")
        break

# # Ask the player for their first descision
# decision = input("Do you wish to take the path (Yes or No): ").lower()


# #Invalid response loop until they give a valid response
# while decision not in ["yes", "no"]:
#     print("invalid choice. please type 'yes' or 'no'.")
#     #opinion for the user to make new desicion 
#     decision = input("do you wish to take the path (yes or no):").lower()

# if decision == "yes":
#     print(f"Brave choice, {player_name}! you step on to the path adventure forward")
# elif decision == "no":
#     print(f"{player_name} , you decide to wait. perhaps courage will find you later.")

