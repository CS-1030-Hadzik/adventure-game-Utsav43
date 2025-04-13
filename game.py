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