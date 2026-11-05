
import time
import sys

def loading_animation(duration_seconds=1):
    end_time = time.time() + duration_seconds
    
    #print("Loading", end="", flush=True)
    
    while time.time() < end_time:
        for dots in [".  ", ".. ", "...", "....", "    "]:
            # \r moves the cursor back to the start of the line
            sys.stdout.write(f"\r{dots}")
            sys.stdout.flush()
            time.sleep(0.4)
            
    print("\r       ")

def show_scene():
    return "Grey dawn light spills over the shore. Cold waves drag at the sand, " \
    "and the storm has left wreckage scattered along the tideline. " \
    "A wooden crate lies half-buried near the rocks. To the north, " \
    "the lighthouse stands dark against the sky, and no beam sweeps the water."
   

def available_actions():
    print("Choose your next action: look, north or quit")
    return input(":>> ").strip().lower()

def is_win(action):
        return action == "look"
    
def apply_action(player):
    valid_actions = ["look", "north", "quit"]
    print(show_scene())
    while True:
        action = available_actions()

        if action not in valid_actions:
            loading_animation()
            print(f"{player}, choose a valid action(look, north or quit).")

        elif action == "quit":
            loading_animation()
            print(f"Game over! Bye {player}")
            break
        
        elif action == "north":
            print("Moving toward the north.")
            loading_animation()
            print("\nWelcome to the Jungle"
                  "\nCross the jungle to get to the lighthouse")
            loading_animation()
            
        elif action == "look":
            loading_animation()
            print(f"""
            {player},you have found a rope in the crate
            Now, move toward the north to get to get
            to the next level
            """)            


def new_game(player):   
    return apply_action(player)
    
