<<<<<<< HEAD
class Player:
    def __init__(self):
        self.health = 100  # Starting health
        self.inventory = []  # Keeps track of items the player collects
    
    def show_health(self):
        print(f"Your current health: {self.health}")

# Functions should be outside the class

def stay_still(player):
    print("You chose to stay still. Your health decreases.")
    player.health -= 10  # Subtract 10 health
    player.show_health()

def explore_cave(player):
    if "lantern" not in player.inventory:
        print("You need a lantern to explore the cave. You lose 10 health.")
        player.health -= 10
    else:
        print("You explore the cave safely.")
    
    player.show_health()

def explore_valley(player):
    if "map" not in player.inventory:
        print("You need a map to find the valley. You lose 10 health.")
        player.health -= 10
    else:
        print("You explore the valley safely.")
    
    player.show_health()

def check_win(player):
    if "treasure" in player.inventory and "rare herbs" in player.inventory:
        print("Congratulations! You found both the treasure and the rare herbs. You win!")
        exit()  # Ends the game

def check_lose(player):
    if player.health <= 0:
        print("You have no health left. You lose!")
        exit()  # Ends the game

# Main game loop
def main():
    print("Welcome to the Adventure Game!")
    print("Your journey begins here...")

    # Create a new player
    player = Player()

    while True:
        print("\nChoose an action:")
        print("1. Stay still")
        print("2. Explore the cave")
        print("3. Explore the valley")
        print("4. Check health")

        choice = input("What will you do? ")

        if choice == "1":
            stay_still(player)
        elif choice == "2":
            explore_cave(player)
        elif choice == "3":
            explore_valley(player)
        elif choice == "4":
            player.show_health()
        
        # Check win or lose after each action
        check_win(player)
        check_lose(player)

# Run the main game loop
if __name__ == "__main__":
    main()
=======
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
            # break

        # Ask the user if they want to continue

    play_again = input("Do you want to continue\n exploring? (yes or no):").lower()

    if play_again != "yes":
        print(f"Thanks for playing, {player_name}\n see you next time") 
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

>>>>>>> e4b972b39b911db741eaa0e601b5536833eb8ebc
