def display(grid):
    print("\n")
    print(f" {grid[0]} | {grid[1]} | {grid[2]} ")
    print("---+---+---")
    print(f" {grid[3]} | {grid[4]} | {grid[5]} ")
    print("---+---+---")
    print(f" {grid[6]} | {grid[7]} | {grid[8]} ")
    print("\n")


def get_input(grid):
    while True:
        choice = input("Enter a position (0-8): ")
        
        if not choice.isdigit():
            print("Invalid input! Please enter a digit between 0 and 8.")
            continue
        
        choice = int(choice)
        if choice not in range(9):
            print("Out of range! Choose a number between 0 and 8.")
        elif grid[choice] != " ":
            print("Cell already occupied! Choose an empty cell.")
        else:
            return choice


def check_winner(grid, player):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  
        (0, 4, 8), (2, 4, 6) 
    ]
    
    return any(grid[a] == grid[b] == grid[c] == player for a, b, c in winning_combinations)


def tic_tac_toe():
    grid = [" "] * 9
    current_player = "X"
    
    print("Welcome to Tic-Tac-Toe!")
    display(grid)
    
    for turn in range(9):
        print(f"Player {1 if current_player == 'X' else 2}'s turn ({current_player})")
        choice = get_input(grid)
        grid[choice] = current_player
        
        display(grid)
        
        if check_winner(grid, current_player):
            print(f"🎉 Player {1 if current_player == 'X' else 2} ({current_player}) wins! Congratulations! 🎉")
            return
        
        current_player = "O" if current_player == "X" else "X"
    
    print("It's a draw! No one wins. 🤝")


tic_tac_toe()
