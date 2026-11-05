# """Drill 1"""
# score = 0
# name = input("what is your player nickname: ")
# print(f"Welcome, {name}")
# print(f"Score: {score}")

# """Drill 2"""
# temperature = 20
# raining = False

# if temperature > 15 and raining == False:
#     print("safe")
# else:
#     print("stay inside")

# """Drill 3"""
# print("choose 1,2 or 3")
# choice = input("Enter your choice: ")

# if choice == "3":
#     print("Bye, game Ended")
# elif choice == "1" or choice == "2":
#     print("Game continues in 30 seconds")
# elif choice == "1":
#     print("Game starting in few minutes")


# else:
#     print("Invalid choice")


# """Drill 4"""
# while True:
#     print("choose 1,2 or 3\n1. north\n2. south\n3. quit")
#     choice = input("Enter your choice: ")
#     if choice == "1" or choice == "north":
#         print("Welcome to the north")
        
#     elif choice == "2" or choice == "south":
#         print("Welcome to the south")
        
#     elif choice == "3" or choice == "quit":
#         print("Good bye!")
#         break
#     else:
#         print("Invalid option, Try again!")
        

# def has_key(inventory):
#     """Return True if 'key' is in the inventory list."""
#     return "key" in inventory
        
# inventory = ["pencil", "pen", "book", "eraser"] 
# print(has_key(inventory))

"""

def main():
    choice_list = ["north", "south"]   
    while True:
        
        choice = get_choice()
    
        if choice in choice_list:
            print(f"Welcome to the {choice}")

        elif choice == "quit":
            print("Good bye!")
            break             
        
        else:
            print("Invalid option, Try again!")
        

def get_choice():
    print("choose north, south or quit")
    choice = input("Enter your choice: ").lower()
    return choice
    
if __name__ == "__main__":
    main()

items = ["map"]
if "rope" not in items:
    items.append("rope")
print(len(items))
print(items)

if "map" in items:
    items.remove("map")
print(len(items))
print(items)
if "rope" not in items:
    items.append("rope")
print(len(items))
print(items)

if "map" in items:
    items.remove("map")
print(len(items))
print(items)


player = {"name": "Maxey", "location": "courtyard", "energy": 10,}
print(player["location"])
player["energy"] -= 2
print(player["energy"])
print(player.get("stats", 0))
print(player["stats"])

selection_list = ["1", "2", "3", "q"]


while True:
    choice = input("Select a choice(1, 2, 3 or q): ").strip().lower()
    if choice not in selection_list:
        print("Invalid option; select 1,2,3 or q")
    elif choice == "q":
        print("good bye")
        break
    elif choice in selection_list:
        print(f"Welcome to no {choice}")       
    else:
        print("Invalid option; select 1,2,3 or q")


while True:
    try:   
        num_input = input("Input a number: ").strip()
        print(int(num_input)+1)
        break
    except ValueError:
        print("Invalid character, only numbers are allowed")
"""