from board import Board
from board import BoardException


def take_move(board):
    print('Please input move [up/down/left/right]')
    move = input()
    if move == 'up':
        board.move_up()
    if move == 'down':
        board.move_down()
    if move == 'right':
        board.move_right()
    if move == 'left':
        board.move_left()
    board.print_board()


def play_puzzle():
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    board = Board([1, 2, 3, 4, 0, 5, 6, 7, 8])
    board.print_board()

    while True:
        if board.tiles == goal:
            print('success!')
            break
        else:
            try:
                take_move(board)
            except BoardException:
                print('Invalid move!')


if __name__ == '__main__':
    play_puzzle()

