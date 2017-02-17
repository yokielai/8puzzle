class Board:

    tiles = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self, input_tiles):
        self.tiles = input_tiles

    def find_gap(self):
        return self.tiles.index(0)

    def can_go(self, gap):
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
