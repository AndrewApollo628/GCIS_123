# 8.3.8

def make_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    print(board[0][0], "|", board[0][1], "|", board[0][2], sep="")
    print("-----")
    print(board[1][0], "|", board[1][1], "|", board[1][2], sep="")
    print("-----")
    print(board[2][0], "|", board[2][1], "|", board[2][2], sep="")

def main():
    my_board = make_board()
    print_board(my_board)

    
main()