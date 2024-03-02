import time
import random

# Define a global variable to store player's inventory
inventory = []

def intro():
    print("Welcome to the Adventure Game!")
    time.sleep(2)
    print("You find yourself standing in front of a dark cave...")
    time.sleep(2)
    print("You can hear strange noises coming from inside.")
    time.sleep(2)
    print("Do you want to enter the cave? (yes/no)")
    choice = input().lower()
    if choice == "yes":
        cave()
    elif choice == "no":
        print("You decide not to enter the cave. Game over!")
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
        intro()

def cave():
    print("As you enter the cave, you see two paths.")
    time.sleep(2)
    print("One path leads to the left, and the other leads to the right.")
    time.sleep(2)
    print("Which path do you choose? (left/right)")
    choice = input().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Invalid choice. Please enter 'left' or 'right'.")
        cave()

def left_path():
    print("You chose the left path.")
    time.sleep(2)
    print("You encounter a bear blocking your way!")
    time.sleep(2)
    print("What do you do? (fight/run)")
    choice = input().lower()
    if choice == "fight":
        if "sword" in inventory:
            print("You use your sword to fight the bear.")
            time.sleep(2)
            print("Congratulations! You defeat the bear and continue on your adventure...")
            time.sleep(2)
            treasure()
        else:
            print("You bravely fight the bear but unfortunately, you are no match for it. Game over!")
    elif choice == "run":
        print("You run away from the bear and manage to escape. You continue on your adventure...")
        time.sleep(2)
        treasure()
    else:
        print("Invalid choice. Please enter 'fight' or 'run'.")
        left_path()

def right_path():
    print("You chose the right path.")
    time.sleep(2)
    print("You walk for a while and suddenly fall into a trap!")
    time.sleep(2)
    print("You find yourself trapped in a dark dungeon. Game over!")

def treasure():
    print("As you explore further, you find a hidden treasure chest!")
    time.sleep(2)
    print("You open the chest and find...")
    time.sleep(2)
    print("A shiny sword!")
    inventory.append("sword")
    time.sleep(2)
    print("You add the sword to your inventory.")
    time.sleep(2)
    print("You continue on your adventure...")
    time.sleep(2)
    print("Congratulations! You win!")

# Start the game
intro()
