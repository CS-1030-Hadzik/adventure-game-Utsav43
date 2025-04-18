# The Player class (keeps track of health, inventory, etc.)
class Player:
    def __init__(self, name):
        self.name = name  # Player's name
        self.health = 100  # Starting health
        self.inventory = []  # Keeps track of items the player collects
        self.has_map = False  # Flag to track if player has map
        self.has_lantern = False  # Flag to track if player has lantern

    def show_health(self):
        print(f"Your current health: {self.health}")

    def has_item(self, item):
        return item in self.inventory

    def add_item(self, item):
        if item not in self.inventory:
            self.inventory.append(item)
            print(f">>> You picked up: {item}!")


# Functions for actions in the game (outside the class)
def explore_dark_woods(player):
    print("You step into the dark woods. The trees whisper as you walk deeper.")
    if not player.has_lantern:
        print("It's too dark to explore the woods properly. You lose 10 health.")
        player.health -= 10
    else:
        print("You explore the woods safely and find some mushrooms to add to your inventory.")
        player.add_item("mushrooms")
    player.show_health()


def explore_mountain_pass(player):
    print("You venture towards the mountain pass.")
    if not player.has_map:
        print("Without a map, you get lost in the mountain pass. You lose 10 health.")
        player.health -= 10
    else:
        print("You follow the map and safely navigate through the mountain pass, finding a hidden cave.")
        explore_cave(player)
    player.show_health()


def explore_cave(player):
    print("You enter the cave. The air is damp and the rocks are slippery.")
    if not player.has_lantern:
        print("It's too dark to explore the cave. You need a lantern. You lose 10 health.")
        player.health -= 10
    else:
        print("You explore the cave safely and discover hidden treasure!")
        player.add_item("treasure")
    player.show_health()


def explore_hidden_valley(player):
    print("You search for the hidden valley.")
    if not player.has_map:
        print("Without a map, you can't find the valley. You lose 10 health.")
        player.health -= 10
    else:
        print("With the map in hand, you find the valley and discover rare herbs.")
        player.add_item("rare herbs")
    player.show_health()


def find_map(player):
    print("You found a map lying on the trail.")
    player.add_item("map")
    player.has_map = True  # Mark that the player has the map


def find_lantern(player):
    print("You found an old lantern hanging on a tree.")
    player.add_item("lantern")
    player.has_lantern = True  # Mark that the player has the lantern


def check_win(player):
    if player.has_item("treasure") and player.has_item("rare herbs"):
        print("🎉 Congratulations! You found both the treasure and the rare herbs. You win!")
        exit()


def check_lose(player):
    if player.health <= 0:
        print("💀 You have no health left. You lose!")
        exit()


# Main game loop
def main():
    print("Welcome to the Adventure Game!")
    player_name = input("What is your name, adventurer?: ")
    print(f"Welcome, {player_name}! Your journey begins now.")

    # Create a Player object
    player = Player(player_name)

    Starting_area = """
    You find yourself in a dark forest.
    The sound of rustling leaves fills the air.
    A faint path lies ahead, leading deeper into the unknown...
    """
    print(Starting_area)

    while True:
        print("\nWhat would you like to do?")
        print("\t1. Take the left path into the dark woods.")
        print("\t2. Take the right path towards the mountain pass (Explore cave).")
        print("\t3. Look for the hidden valley.")
        print("\t4. Stay where you are.")
        print("\t5. Check health.")
        print("\t6. Search around for useful items.")

        decision = input("Choose (1-6): ")

        if decision == "1":
            explore_dark_woods(player)
        elif decision == "2":
            explore_mountain_pass(player)
        elif decision == "3":
            explore_hidden_valley(player)
        elif decision == "4":
            print(f"{player.name}, you chose to stay still. Your health decreases.")
            player.health -= 10
            player.show_health()
        elif decision == "5":
            player.show_health()
            print("Your inventory:", player.inventory)
        elif decision == "6":
            print("You search your surroundings...")
            import random
            item_found = random.choice(["map", "lantern", "nothing"])
            if item_found == "map":
                find_map(player)
            elif item_found == "lantern":
                find_lantern(player)
            else:
                print("You didn’t find anything useful.")
        else:
            print("Invalid choice. Please choose a number between 1 and 6.")

        check_win(player)
        check_lose(player)

        play_again = input("Do you want to continue exploring? (yes or no): ").lower()
        if play_again != "yes":
            print(f"Thanks for playing, {player.name}. See you next time!")
            break


# Run the main game loop
if __name__ == "__main__":
    main()
