import random
import time

print("""
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          
▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ 
▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░▌          ▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀█░▌
▐░▌          ▐░▌     ▐░▌  ▐░▌       ▐░▌▐░▌                    ▐░▌
▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ ▐░▌       ▐░▌▐░▌           ▄▄▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀         ▀  ▀            ▀▀▀▀▀▀▀▀▀▀▀ 
      """)

def get_dice_art(dice_value):
    dice_art = {
        1: ["┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘"],
        2: ["┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘"],
        3: ["┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘"],
        4: ["┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘"],
        5: ["┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘"],
        6: ["┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘"]
    }
    return dice_art[dice_value]

def display_dice(dice1, dice2):
    dice1_art = get_dice_art(dice1)
    dice2_art = get_dice_art(dice2)

    for i in range(5):
        print(f"{dice1_art[i]}  {dice2_art[i]}")

def roll_dice():
    ...print("\nRolling the dice")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n")
          
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    display_dice(dice1, dice2)
    return dice1 + dice2

def play_craps():
    print("Welcome to Craps!")
    print("Press Enter to roll the dice...")
    input()

    total = roll_dice()
    print(f"\nYou rolled: {total}")

    if total in (7, 11):
        print("You win!")
        return
    elif total in (2, 3, 12):
        print("You lose!")
        return
    
    point = total
    print(f"Your point is {point}")

    while True:
        print("\nPress Enter to roll again")
        input()
        total = roll_dice()
        print(f"\nYou rolled: {total}")

        if total == point:
            print("You win!")
            break
        elif total == 7:
            print("You lose!")
            break

if __name__ == "__main__":
    while True:
        play_craps()
        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again != 'y':
            print("\nThanks for playing!")
            break