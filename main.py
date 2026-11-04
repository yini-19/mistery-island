from game_logic.game import new_game
from game_logic.game import loading_animation

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
    return input("Select option(1, 2, 3 or 4): ")
    


def main():

    while True:
        choice = welcome_display(name)
        name = input("Choose your gaming nickname: ").strip().lower().capitalize()
        available_choices = ["1", "2", "3", "4"]
        
        loading_animation()
        
        if choice not in available_choices:
            loading_animation()
            print("Invalid choice: choose between 1, 2, 3 and 4")
        elif choice == "4":
            loading_animation()
            print("Farewell from mistery-island")
            break
        elif choice == "1":
            print(new_game(name))
            

        else:
            loading_animation()
            print("invalid choice")
   
   
   
      
if __name__=="__main__":
    main()