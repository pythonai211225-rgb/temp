game_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def welcome():
    print('Welcome to Tic Tac Toe!')


def board_print():
    print(f'\n {game_board[0]} | {game_board[1]} | {game_board[2]} ')
    print('---+---+---')
    print(f' {game_board[3]} | {game_board[4]} | {game_board[5]}')
    print('---+---+---')
    print(f' {game_board[6]} | {game_board[7]} | {game_board[8]} \n')


def player_x_choice():
    while True:
        try:
            choice_x = int(input("Please choose a spot (1-9): "))
            if 1 <= choice_x <= 9:
                index = choice_x - 1
                if game_board[index] != 'x' and game_board[index] != 'o':
                    game_board[index] = 'x'
                    break
                else:
                    print("Spot taken, try another one.")
            else:
                print("Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number to choose from the available spots on the board.")


def player_o_choice():
    while True:
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


def x_win():
    if (game_board[0] == game_board[1] == game_board[2] == 'x' or
            game_board[3] == game_board[4] == game_board[5] == 'x' or
            game_board[6] == game_board[7] == game_board[8] == 'x' or
            game_board[0] == game_board[3] == game_board[6] == 'x' or
            game_board[1] == game_board[4] == game_board[7] == 'x' or
            game_board[2] == game_board[5] == game_board[8] == 'x' or
            game_board[0] == game_board[4] == game_board[8] == 'x' or
            game_board[2] == game_board[4] == game_board[6] == 'x'):
        return True
    else:
        return False


def o_win():
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
    return all(spot == 'x' or spot == 'o' for spot in game_board)


welcome()

while True:
    board_print()
    print("flip a coin ;)   x goes first!")

    player_x_choice()
    if x_win():
        board_print()
        print("X WINS!")
        break
    if check_draw():
        board_print()
        print("It's a draw!")
        break

    board_print()
    print("o's turn!")

    player_o_choice()
    if o_win():
        board_print()
        print("O WINS!")
        break
    if check_draw():
        board_print()
        print("It's a draw!")
        break