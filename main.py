import time
from adventures import north_adventure, east_adventure, south_adventure, west_adventure
from dictionary import description, game_exit_msg

# Welcome message and title of the game.
print("|----------------------------|")
print("| The Mathematical Labyrinth |")
print("|----------------------------|" + "\n")

# Display description of the adventure.
def game_description():
    for line in description:
        print(line)
    print()
    
# Display message when player exits game.
def game_exit():
    print(game_exit_msg["message"])

# Main game loop.
def game_loop():
    run = True
    while run:
        # Declare the list of direction a player can choose from.
        directions = ["north", "east", "south", "west", "EXIT"]
        print("\nYou are presented with 4 directions, or exit: ")
        
        # Iterate through the list and print the array items.
        for index, direction in enumerate(directions, start=1):
            print(f"{index}. {direction}")                
        
        # Ask for player's choice of direction.
        dirChoice = input("\nWhat is your choice? (1, 2, 3, 4, 5)\n-> ")
        
        # Convert to int if possible, otherwise keep as string and convert it to lowercase.
        try: 
            dirChoice = int(dirChoice)
        except ValueError:
            dirChoice = dirChoice.lower()

        # Logic do select adventure based on player's input.
        if dirChoice == 1 or dirChoice == "north":
            time.sleep(0.5)
            north_adventure()
        elif dirChoice == 2  or dirChoice == "east":
            time.sleep(0.5)
            east_adventure()
        elif dirChoice == 3  or dirChoice == "south":
            time.sleep(0.5)
            south_adventure()
        elif dirChoice == 4  or dirChoice == "west":
            time.sleep(0.5)
            west_adventure()
        elif dirChoice == 5  or dirChoice == "exit":
            time.sleep(0.5)
            game_exit()
            run = False
        else:
            print("Are you choosing the correct direction?")
            

# Ask player if they want to play the game.
def play_game():
    # Ask player if they want to play or not.
    playGame = input("Do you want to solve the mysteries? y/n:\n-> ")
    if playGame.lower() == 'y':
        game_loop()
    else:
        game_exit()

game_description()
play_game()