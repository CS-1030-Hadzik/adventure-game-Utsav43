# The Player class (keeps track of health, inventory, etc.)
class Player:
    def __init__(self):
        self.health = 100  # Starting health
        self.inventory = []  # Keeps track of items the player collects
     
    def show_health(self):
        print(f"Your current health: {self.health}")

# Functions for actions in the game (outside the class)
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

# Main game loop (combining player name and interactions with the game mechanics)
def main():
    print("Welcome to the Adventure Game!")
    player_name = input("What is your name adventurer??: ")
    print(f"Welcome, {player_name}! Your journey begins now.")

    player = Player()  # Create a new player

    Starting_area = """
    You find yourself in a dark forest.
    The sound of rustling leaves fills the air.
    A faint path lies ahead, leading deeper into the unknown...
    """
    print(Starting_area)

    while True:
        print("\nYou see two paths ahead: ")
        print("\t1. Take the left path into the dark woods.")
        print("\t2. Take the right path towards the mountain pass.")
        print("\t3. Stay where you are.")
        print("\t4. Check health.")

        decision = input("What will you do (1, 2, 3, 4): ")

        if decision == "1":
            print(f"{player_name}, you step into the dark woods. The trees whisper as you walk deeper.")
            stay_still(player)
        elif decision == "2":
            print(f"{player_name}, you make your way towards the mountain pass, feeling the cold wind against your face.")
            explore_cave(player)
        elif decision == "3":
            print(f"{player_name}, you stay still, listening to the distant sounds of the forest.")
            stay_still(player)
        elif decision == "4":
            player.show_health()  # Check health option
        else:
            print("Invalid choice! Please choose 1, 2, 3, or 4.")

        # Check for win or lose conditions
        check_win(player)
        check_lose(player)

        # Ask the user if they want to continue
        play_again = input("Do you want to continue exploring? (yes or no): ").lower()

        if play_again != "yes":
            print(f"Thanks for playing, {player_name}. See you next time!")
            break

# Run the main game loop
if __name__ == "__main__":
    main()
