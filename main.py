import time
import sys
from game_logic.game import new_game

def loading_animation(duration_seconds=5):
    end_time = time.time() + duration_seconds
    
    print("Loading", end="", flush=True)
    
    while time.time() < end_time:
        for dots in [".  ", ".. ", "...", "   "]:
            # \r moves the cursor back to the start of the line
            sys.stdout.write(f"\rGame loading{dots}")
            sys.stdout.flush()
            time.sleep(0.4)
            
    print("\r    ")

loading_animation()

def welcome_display(name):

    print(f"""
=========================================
    {name}, WELCOME TO MYSTERY-ISLAND
=========================================
    1. START GAME
    2. MAP/LOCATIONS
    3. INSTRUCTIONS/ABOUT
    4. QUIT
""")
    return input("Select option(1, 2 or 3)")
    


def main():
    name = input("Choose your gaming nickname: ").strip().lower().capitalize()
    choice = welcome_display(name)
    available_choices = ["1", "2", "3", "4"]

    while True:
        if choice not in available_choices:
            print("Invalid choice: choose between 1, 2, 3 and 4")
        elif choice == "4":
            print("Farewell from mistery-island")
            break
        elif choice == "1":
            new_game()
   
   
   
    return    
if __name__=="__main__":
    main()