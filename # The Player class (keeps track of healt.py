# The Player class (keeps track of health, inventory, etc.)
class Player:
    def __init__(self):
        self.health = 100  # Starting health
        self.inventory = []  # Keeps track of items the player collects

    def show_health(self):
        print(f"Your current health: {self.health}")

    def has_item(self, item):
        return item in self.inventory

    def add_item(self, item):
        if item not in self.inventory:
            self.inventory.append(item)
            print(f">>> You picked up: {item}!")


# Functions for actions in the game (outside the class)
def stay_still(player):
    print("You chose to stay still. Your health decreases.")
    player.health -= 10
    player.show_health()

def explore_cave(player):
    # TODO: In the cave choice:
    #       - If player.has_lantern is True: allow entry and add "treasure" to inventory
    #       - Else: display a message that it’s too dark
    if not player.has_item("lantern"):
        print("It's too dark to explore the cave. You need a lantern. You lose 10 health.")
        player.health -= 10
    else:
        print("You explore the cave safely and discover hidden treasure!")
        player.add_item("treasure")
    player.show_health()

def explore_valley(player):
    # TODO: In the valley choice:
    #       - If player.has_map is True: allow entry and add "rare herbs" to inventory
    #       - Else: display a message that you can’t find the valley
    if not player.has_item("map"):
        print("You can't find the valley without a map. You lose 10 health.")
        player.health -= 10
    else:
        print("You explore the hidden valley and find rare herbs!")
        player.add_item("rare herbs")
    player.show_health()

def find_map(player):
    print("You found a map lying on the trail.")
    player.add_item("map")

def find_lantern(player):
    print("You found an old lantern hanging on a tree.")
    player.add_item("lantern")

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

    player = Player()

    Starting_area = """
    You find yourself in a dark forest.
    The sound of rustling leaves fills the air.
    A faint path lies ahead, leading deeper into the unknown...
    """
    print(Starting_area)

    # Add starting items for testing, or let the player find them later
    # player.add_item("lantern")
    # player.add_item("map")

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
            print(f"{player_name}, you step into the dark woods. The trees whisper as you walk deeper.")
            stay_still(player)
        elif decision == "2":
            explore_cave(player)
        elif decision == "3":
            explore_valley(player)
        elif decision == "4":
            stay_still(player)
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
            print(f"Thanks for playing, {player_name}. See you next time!")
            break

# Run the main game loop
if __name__ == "__main__":
    main()
