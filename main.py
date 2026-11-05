from game_logic.game import new_game
from game_logic.game import loading_animation, show_scene

def get_choice(name):
    print(f"""
=========================================
    {name}, WELCOME TO MYSTERY-ISLAND
=========================================
    1. START GAME
    2. MAP/LOCATIONS(shows your next location)
    3. INSTRUCTIONS
    4. QUIT
""")
    return input("Select option(1, 2, 3 or 4): ").strip()

def map_locations():
    return """ 
    -------------------------------- 
    //===MAP OF MYSTERY-ISLAND===//
    --------------------------------
    Beach -> Jungle -> Cave -> Old bridge -> Light house
    """ 

def instructions():
    return """    
    -------------------------------   
    //===GAMING INSTRUCTIONS===//
    -------------------------------
    -Press 1 to start new game.
    -Press 2 for locations map.
    -Press 3 for instructions to the game.
    -Press 4 to quit the game.
    """

def main():
    available_choices = ["1", "2", "3", "4"]
    
    print(instructions())
    name = input("Choose your gaming nickname: ").strip().lower().capitalize()

    while True:
        choice = get_choice(name)
        
        if choice not in available_choices:
            print("Invalid choice: choose between 1, 2, 3 and 4")
        elif choice == "4":
            print("Farewell from mystery-island")
            break
        elif choice == "1":
            loading_animation()
            new_game(name)
        elif choice == "2":
            loading_animation()
            print(map_locations())   
        else:
            loading_animation()
            print(instructions())
   
   
   
      
if __name__=="__main__":
    main() 