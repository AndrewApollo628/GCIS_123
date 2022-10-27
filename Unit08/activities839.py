# 8.3.9

def make_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    print(board[0][0], "|", board[0][1], "|", board[0][2], sep="")
    print("-----")
    print(board[1][0], "|", board[1][1], "|", board[1][2], sep="")
    print("-----")
    print(board[2][0], "|", board[2][1], "|", board[2][2], sep="")
    
def make_move(board, symbol):
    no_move = True
    while no_move:
        try:
            move = input("Enter move (row col): ")
            tokens = move.split()
            row = int(tokens[0])
            col = int(tokens[1])

            if board[row][col] == " ":
                board[row][col] = symbol
                no_move = False
            else:
                print("Invalid move. Please try again.")
        except IndexError:
            print("Invalid move. Please try again.")
    print_board(board)

def main():
    my_board = make_board()
    print_board(my_board)
    make_move(my_board, "X")
    make_move(my_board, "O")

    
main()