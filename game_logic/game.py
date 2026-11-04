
import time
import sys

def loading_animation(duration_seconds=2):
    end_time = time.time() + duration_seconds
    
    print("Loading", end="", flush=True)
    
    while time.time() < end_time:
        for dots in [".  ", ".. ", "...", "   "]:
            # \r moves the cursor back to the start of the line
            sys.stdout.write(f"\rloading{dots}")
            sys.stdout.flush()
            time.sleep(0.4)
            
    #print("\r  ")

def beach_scene():
    print("\nYou stand on a quiet beach at dawn. Pale waves roll over the sand, "
      "and gulls circle above a half-buried wooden crate. "
      "A weathered lighthouse watches from the rocks to the north.")

def available_actions():
    print("Choose your next action: look, north or quit")
    return input(":>> ").strip().lower()

def is_win(player):
    return f"""{player},you have found a rope in the crate
        {player},You win!
        Level completed
        Moving to the next level"""
    
def apply_action(player):
    valid_actions = ["look", "north", "quit"]
   
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
            print("Moving toward the north."
                  "\nWrong move, Energy dropping!"
                  "\nfind rope in crate first!")
            loading_animation()
            

        elif action == "look":
            loading_animation()
            print(is_win(player))
            

        else:
            print("Invalid action, try again.")




def new_game(player):
    beach_scene()
    result = apply_action(player)
    return result
