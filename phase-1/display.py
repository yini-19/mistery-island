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
        

def has_key(inventory):
    """Return True if 'key' is in the inventory list."""
    return "key" in inventory
        
inventory = ["pencil", "pen", "book", "eraser"] 
print(has_key(inventory))



def main():
    
    while True:
    
        choice = get_choice()
    
        if choice == "north":
            print("Welcome to the north")
                
        elif choice == "south":
            print("Welcome to the south")
                
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