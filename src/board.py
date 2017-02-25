from utility import *

class Board:

    def __init__(self, input_tiles):
        self.tiles = input_tiles


    def reset(self):
        self.tiles = [1, 2, 3, 4, 0, 5, 6, 6, 7, 8]


    def move_up(self):
        gap = self.gap()
        can_go = self.can_go()
        if can_go[0]:
            self.tiles[gap] = self.tiles[gap - 3]
            self.tiles[gap - 3] = 0
        else:
            raise Exception('invalid move')

    def move_down(self):
        gap = self.gap()
        can_go = self.can_go()
        if can_go[2]:
            self.tiles[gap] = self.tiles[gap + 3]
            self.tiles[gap + 3] = 0
        else:
            raise Exception('invalid move')

    def move_left(self):
        gap = self.gap()
        can_go = self.can_go()
        if can_go[3]:
            self.tiles[gap] = self.tiles[gap - 1]
            self.tiles[gap - 1] = 0
        else:
            raise Exception('invalid move')


    def move_right(self):
        gap = self.gap()
        can_go = self.can_go()
        if can_go[1]:
            self.tiles[gap] = self.tiles[gap + 1]
            self.tiles[gap + 1] = 0
        else:
            raise Exception('invalid move')


    def gap(self):
        return self.tiles.index(0)


    def can_go(self):
        gap = self.gap()
        if (gap - 3) <= -1:
            go_up = False
        else:
            go_up = True

        if (gap + 3) > 9:
            go_down = False
        else:
            go_down = True

        if ((gap + 1) % 3) == 0:
            go_right = False
        else:
            go_right = True

        if ((gap + 3) % 3) == 0:
            go_left = False
        else:
            go_left = True

        return [go_up, go_right, go_down, go_left]


    def print_board(self):
        print str(self.tiles[0]) + ' ' + str(self.tiles[1]) + ' ' + str(self.tiles[2])
        print str(self.tiles[3]) + ' ' + str(self.tiles[4]) + ' ' + str(self.tiles[5])
        print str(self.tiles[6]) + ' ' + str(self.tiles[7]) + ' ' + str(self.tiles[8])


