# where computer is a record system 

player1 = []  #player one choices 
player2 = []  #player two choices
choices = []  #list of how many flags you can take

print(f"--- THAI 21 ---")
flags = int(input("How many flags are there total? "))  #allowing people to set the number of flags
choice = input("How many flags can you take?(ex. 123 as you can take 1, 2, or 3 flags) ")  #allowing people to set number of flags you can take
for char in choice:
    choices.append(int(char))  #putting the input in seperate indexes

print(f"\nRemaning flags left: {flags}")
while flags > 0:

    #player one inputs
    pick1 = int(input("Player 1, How many flags do you want to take? "))
    while pick1 not in choices:  #if the pick isn't in choices, then ask them to go again
        print("***That isn't a valid number!***\n")
        print(f"Remaning flags left: {flags}")
        pick1 = int(input("Player 1, How many flags do you want to take? "))
    player1.append(pick1)  #add to the record of player one 
    flags -= pick1         #decrease the total flags 
    print(f"\nRemaning flags left: {flags}")
    if flags <= 0:  #if flags is zero after there pick, then they win 
        print("\n\nPlayer 1 has won!")
        break
    
    #player two inputs
    pick2 = int(input("Player 2, How many flags do you want to take? "))
    while pick2 not in choices:
        print("***That isn't a valid number!***\n")
        print(f"Remaning flags left: {flags}")
        pick2 = int(input("Player 2, How many flags do you want to take? "))
    player2.append(pick2)
    flags -= pick2
    print(f"\nRemaning flags left: {flags}")
    if flags <= 0:
        print("\n\nPlayer 2 has won!")

#listing player picks
print("List of picks:")
print(f"Player 1: {player1}")
print(f"Player 2: {player2}")
