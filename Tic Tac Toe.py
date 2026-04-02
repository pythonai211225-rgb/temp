# ======================= defining game environment =============================

# This list represents the 9 squares on the board. We use strings so we can print them.
game_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
# index ->     0    1    2    3    4    5    6    7    8

def board_print():
    print(f'\n {game_board[0]} | {game_board[1]} | {game_board[2]} ')
    print('---+---+---')  #
    print(f' {game_board[3]} | {game_board[4]} | {game_board[5]}')
    print('---+---+---')
    print(f' {game_board[6]} | {game_board[7]} | {game_board[8]} \n')

def welcome():
    print('Welcome to Tic Tac Toe!')

# ================= defining user turn choices ===============================

def player_x_choice():
    while True:  # Keep asking until the player provides a valid move
        try:  # try doing the following, if encountered an error, go to except...
            choice_x = int(input("Please choose a spot (1-9): "))  # takes number from user as int (if not int- error)
            if 1 <= choice_x <= 9:  # Check if the number is actually on the board
                index = choice_x - 1  # save in variable, subtract 1 because lists start at index 0
                # Check if the spot is still a number - aka empty (not already an 'x' or 'o')
                if game_board[index] != 'x' and game_board[index] != 'o':
                    game_board[index] = 'x'  # Update the board in chosen spot
                    break  # Exit the 'while True' loop because the move was successful
                else: # Error - spot is occupied
                    print("Spot taken, try another one.")
            else: # Error - number is out of range
                print("Please enter a number between 1 and 9.")
        except ValueError: # program tried and failed to meet condition ->except the error and do the following:
            print("Invalid input. Please enter a number to choose from the available spots on the board.")  # Prevents crash if user types letters


def player_o_choice():
    while True:  # Same logic as player_x_choice()
        try:
            choice_o = int(input("Player O! Please choose a spot (1-9): "))
            if 1 <= choice_o <= 9:
                index = choice_o - 1
                if game_board[index] != 'x' and game_board[index] != 'o':
                    game_board[index] = 'o'
                    break
                else:
                    print("Spot taken, try another one.")
            else:
                print("Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number to choose from the available spots on the board.")


# ================== defining game possible outcomes ==================================

def x_win():
    # Check all 8 possible ways x could win (3 horizontal, 3 vertical, 2 diagonal)
    if (game_board[0] == game_board[1] == game_board[2] == 'x' or
            game_board[3] == game_board[4] == game_board[5] == 'x' or
            game_board[6] == game_board[7] == game_board[8] == 'x' or
            game_board[0] == game_board[3] == game_board[6] == 'x' or
            game_board[1] == game_board[4] == game_board[7] == 'x' or
            game_board[2] == game_board[5] == game_board[8] == 'x' or
            game_board[0] == game_board[4] == game_board[8] == 'x' or
            game_board[2] == game_board[4] == game_board[6] == 'x'):
        return True  # Return True if any of these patterns match
    else:
        return False  # Otherwise, return False


def o_win():
    # Same logic as x_win, but checking for the 'o' character
    if (game_board[0] == game_board[1] == game_board[2] == 'o' or
            game_board[3] == game_board[4] == game_board[5] == 'o' or
            game_board[6] == game_board[7] == game_board[8] == 'o' or
            game_board[0] == game_board[3] == game_board[6] == 'o' or
            game_board[1] == game_board[4] == game_board[7] == 'o' or
            game_board[2] == game_board[5] == game_board[8] == 'o' or
            game_board[0] == game_board[4] == game_board[8] == 'o' or
            game_board[2] == game_board[4] == game_board[6] == 'o'):
        return True
    else:
        return False


def check_draw():
    # A draw happens if no one has won but there are no numbers left in the list (aka no empty spots on list)
    # The 'all' function returns True if every spot is filled with 'x' or 'o'
    return all(spot == 'x' or spot == 'o' for spot in game_board)


# ========================== game loop ================================

welcome()  # Run the welcome function once at the start

while True:  # The main game loop, keeps running until one player wins\draw.
    board_print()  # Show the board

    print("flip a coin ;)   x goes first!")

    player_x_choice()  # Get Player x's move
    if x_win():  # Check if that move won the game
        board_print()  # Show final board
        print("X WINS!")
        break  # win! Stop the game loop
    if check_draw():  # Check if that move resulted in a tie
        board_print()
        print("It's a draw!")
        break # draw. breaks game loop

    board_print()  # Show the updated board
    print("o's turn!")

    player_o_choice()  # Get Player o's move
    if o_win():  # Check if that move won the game
        board_print()  # Show final board
        print("O WINS!")
        break  # win! Stop the game loop
    if check_draw():  # Check if that move resulted in a tie
        board_print()
        print("It's a draw!")
        break # draw. breaks game loop