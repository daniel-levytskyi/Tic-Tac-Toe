turn = 0

nums = [" ", "1", "2", "3"]
row1 = ["A", " ", " ", " "]
row2 = ["B", " ", " ", " "]
row3 = ["C", " ", " ", " "]

#print the table
def make_board():
    table = [nums, row1, row2, row3]
    for x in table:
        print(x)

def player_num():
    if turn % 2 == 0:
        return "X"
    else: 
        return "O"

def get_choice():
    global choice
    choice = input("Make a choice: ")

def game_loop():
    check_row()
    check_column()
    check_diagonal()
    make_board()
    get_choice()
    place_marker()

def place_marker():
    global turn
    if "A" in choice or "a" in choice:
        if "1" in choice:
            if row1[1] != " ":
                print("Spot taken!")
                player_num()
            else:    
                row1[1] = player_num()
                turn += 1
        elif "2" in choice:
            if row1[2] != " ":
                print("Spot taken!")
                player_num()
            else:    
                row1[2] = player_num()
                turn += 1
        elif "3" in choice:
            if row1[3] != " ":
                print("Spot taken!")
                player_num()
            else:    
                row1[3] = player_num()
                turn += 1
    if "B" in choice or "b" in choice:
        if "1" in choice:
            if row2[1] != " ":
                print("Spot taken!")
                player_num()
            else:    
                row2[1] = player_num()
                turn += 1
        elif "2" in choice:
            if row2[2] != " ":
                print("Spot taken!")
                player_num()
            else:    
                row2[2] = player_num()
                turn += 1
        elif "3" in choice:
            if row2[3] != " ":
                print("Spot taken!")
                player_num()
            else:    
                row2[3] = player_num()
                turn += 1
    if "C" in choice or "c" in choice:
        if "1" in choice:
            if row3[1] != " ":
                print("Spot taken!")
                player_num()
            else:    
                row3[1] = player_num()
                turn += 1
        elif "2" in choice:
            if row3[2] != " ":
                print("Spot taken!")
                player_num()
            else:    
                row3[2] = player_num()
                turn += 1
        elif "3" in choice:
            if row3[3] != " ":
                print("Spot taken!")
                player_num()
            else:    
                row3[3] = player_num()
                turn += 1

def check_row():
    if row1[1] == row1[2] == row1[3] != " " or row2[1] == row2[2] == row2[3] != " " or row3[1] == row3[2] == row3[3] != " ":
        print(f"{row1[1]} is the winner!")
        quit()
def check_column():
    if row1[1] == row2[1] == row3[1] != " " or row1[2] == row2[2] == row3[2] != " " or row1[3] == row2[3] == row3[3] != " ":
        print(f"{row1[1]} is the winner!")
        quit()
def check_diagonal():
    if row1[1] == row2[2] == row3[3] != " " or row1[3] == row2[2] == row3[1] != " ":
        print(f"{row1[1]} is the winner!")
        quit()

while True:
    game_loop()
