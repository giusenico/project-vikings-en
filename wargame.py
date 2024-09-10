from vikingsClasses import Soldier, Viking, Saxon, War
import random
import time

def display_round_info(round, war):
    print("\n" + "="*40)  # Visual separator for readability
    print(f"Round {round}")
    print("="*40)
    print(f"Viking Army: {len(war.vikingArmy)} warriors remaining")
    print(f"Saxon Army: {len(war.saxonArmy)} warriors remaining")
    print("="*40)

def start_game():
    soldier_names = ["albert", "andres", "archie", "dani", "david", "gerard", "german", "graham", "imanol", "laura"]

    # Ensure the user inputs a positive integer for Vikings
    while True:
        try:
            num_vikings = int(input("\nHow many Vikings do you want to create? "))
            if num_vikings <= 0:
                raise ValueError
            break
        except ValueError:
            print("\nInvalid input! Please enter a valid positive number greater than zero.")

    # Ensure the user inputs a positive integer for Saxons
    while True:
        try:
            num_saxons = int(input("\nHow many Saxons do you want to create? "))
            if num_saxons <= 0:
                raise ValueError
            break
        except ValueError:
            print("\nInvalid input! Please enter a valid positive number greater than zero.")

    war = War()

    # Viking creation
    for i in range(num_vikings):
        viking_name = random.choice(soldier_names)
        viking_health = 100
        viking_strength = random.randint(0, 100)
        war.addViking(Viking(viking_name, viking_health, viking_strength))

    # Saxon creation
    for i in range(num_saxons):
        saxon_health = 100
        saxon_strength = random.randint(0, 100)
        war.addSaxon(Saxon(saxon_health, saxon_strength))

    # Debugging: Verify that the armies were created correctly
    print(f"\nVikings created: {len(war.vikingArmy)}")
    print(f"Saxons created: {len(war.saxonArmy)}")

    # Start the battle loop
    round = 0
    while war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
        war.vikingAttack()
        
        # Check the status after the Viking attack
        if war.showStatus() != "Vikings and Saxons are still in the thick of battle.":
            break

        war.saxonAttack()

        # Display detailed round information
        display_round_info(round, war)
        
        round += 1
        time.sleep(2)  # Wait 2 seconds between each round for better visualization


    # Print the final result
    print("\n" + war.showStatus())

# Prompt the user to press Enter to start
input("\nPress enter to start a new game ")

# Main loop to repeat games
while True:
    start_game()

    # Ensure the user enters 'Y' or 'N'
    while True:
        play_again = input("\nDo you want to play another game? (Y/N): ").strip().lower()
        if play_again in ['y', 'n']:
            break
        else:
            print("\nInvalid input! Please enter 'Y' to play again or 'N' to quit.")

    if play_again == 'n':
        print("\nThank you for playing the game!")
        break
