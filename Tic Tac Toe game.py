import os
import json

# Display the Tic Tac Toe board
def display_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

# Check for a win or tie
def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    # Check for tie
    for row in board:
        if " " in row:
            return None

    return "Tie"

# Save the game state to a file
def save_game(board, current_player):
    with open("tic_tac_toe_save.json", "w") as file:
        json.dump({"board": board, "current_player": current_player}, file)
    print("Game saved successfully!")

# Load the game state from a file
def load_game():
    if os.path.exists("tic_tac_toe_save.json"):
        with open("tic_tac_toe_save.json", "r") as file:
            data = json.load(file)
            return data["board"], data["current_player"]
    else:
        return None, None

# Main game function
def play_game():
    print("Welcome to Tic Tac Toe!")

    # Load the game state if available
    board, current_player = load_game()

    if board is None:
        # Initialize a new game
        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = "X"

    while True:
        display_board(board)
        print(f"Player {current_player}'s turn")

        # Get the player's move
        try:
            row, col = map(int, input("Enter your move (row and column, 1-3) separated by space: ").split())
            row -= 1
            col -= 1

            if board[row][col] == " ":
                board[row][col] = current_player
            else:
                print("Cell already occupied. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Enter row and column as numbers between 1 and 3.")
            continue

        # Check for a winner
        result = check_winner(board)
        if result:
            display_board(board)
            if result == "Tie":
                print("The game is a tie!")
            else:
                print(f"Player {result} wins!")
            if os.path.exists("tic_tac_toe_save.json"):
                os.remove("tic_tac_toe_save.json")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

        # Offer to save the game
        choice = input("Do you want to save the game and exit? (yes/no): ").strip().lower()
        if choice == "yes":
            save_game(board, current_player)
            break

if __name__ == "__main__":
    play_game()
