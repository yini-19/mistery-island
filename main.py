import time
import sys

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

def menu_display(name):

    print(f"""
=========================================
    {name}, WELCOME TO MYSTERY-ISLAND
=========================================
    1. START GAME
    2. MOVEMENTS/ACTIONS
    3. MAP/LOCATIONS
    4. QUIT
""")
    

def main():
    name = input("Choose your gaming nickname: ").strip().lower().capitalize()
    return    
if __name__=="__main__":
    main()