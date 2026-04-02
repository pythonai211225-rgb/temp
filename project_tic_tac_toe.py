def create_board():
    board =  ['1','2','3','4','5','6','7','8','9']
    return board

def print_board(board):
    for i in range(0,9,3):
        print(board[i],board[i+1],board[i+2], sep=' | ')
        if i < 6:
            print('--+---+--')
    return board

def get_move(player, board):
    while True:
        move = input(f"{player}'s turn. Enter a number (1-9): ")
        if move in board:
            return int(move)
        else:
            print("Invalid move. Please try again.")

def make_move(board, position, symbol):
    board[position - 1] = symbol
    return board

def check_winner(board, symbol):
    return any(
        board[a] == board[b] == board[c] == symbol
        for a, b, c in [
            (0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)
        ]
    )

def is_tie(board):
    return all(cell in ['X', 'O'] for cell in board)


def switch_player(current):
    return 'O' if current == 'X' else 'X'

def play_game():
    board = create_board()
    current_player = 'X'

    while True:
        print_board(board)
        move = get_move(current_player, board)
        make_move(board, move, current_player)

        if check_winner(board, current_player):
            print_board(board)
            print(f"{current_player} wins!")
            break

        if is_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = switch_player(current_player)


if __name__ == "__main__":
    play_game()
