import numpy as np
import sys


class Tile:
    def __init__(self, id, img):
        self.id = id
        self.img = img

        self.make_edges()
        self.friends = [None for _ in range(4)]

    def make_edges(self):
        e1 = self.img[0, :][::-1]
        e2 = self.img[:, 0]
        e3 = self.img[-1, :]
        e4 = self.img[:, -1][::-1]
        self.edges = [hash(tuple(i)) for i in (e1, e2, e3, e4)]

    def __repr__(self):
        return str(self.id)

    def __eq__(self, other):
        if isinstance(other, Tile):
            return self.id == other.id
        elif isinstance(other, int):
            return self.id == other

    def flip(self):
        self.img = self.img.T
        self.make_edges()
        self.permute_friends((1, 0, 3, 2))

    def lr_flip(self):
        self.img = self.img[:, ::-1]
        self.permute_friends((0, 3, 2, 1))

    def tb_flip(self):
        self.img = self.img[::-1, :]
        self.permute_friends((2, 1, 0, 3))

    def rotate(self):
        self.img = np.rot90(self.img)
        self.permute_friends((3, 0, 1, 2))

    def permute_friends(self, order):
        self.friends = [self.friends[i] for i in order]

    def core(self):
        return self.img[1: -1, 1: -1]

    def match(self, other):
        for turn in range(2):
            for i, mine in enumerate(self.edges):
                for j, their in enumerate(other.edges):
                    if mine == their:
                        self.befriend(other, i, j)
                        return
            other.flip()

    def befriend(self, other, mine, their):
        self.friends[mine] = other
        other.friends[their] = self

    def is_corner(self):
        return sum([i is not None for i in self.friends]) == 2


class Board:
    def __init__(self, size, start):
        self.s = start.img.shape[0] - 2
        self.board = np.zeros((size, size), dtype=Tile)
        self.img = np.zeros((size * self.s, size * self.s))

        self.board[0, 0] = start
        self.img[:self.s, :self.s] = start.core()

    def insert_right(self, x, y):
        if y == 0:
            above = None
        else:
            above = self.board[y - 1, x + 1]
        left = self.board[y, x]
        new = left.friends[3]
        while new.friends[1] != left:
            new.rotate()
        if new.friends[0] != above:
            new.tb_flip()
        self.board[y, x + 1] = new
        s = self.s
        x += 1
        self.img[y * s: (y + 1) * s, x * s: (x + 1) * s] = new.core()

    def insert_down(self, y):
        if y == self.board.shape[0] - 1:
            return
        above = self.board[y, 0]
        new = above.friends[2]
        while new.friends[0] != above:
            new.rotate()
        if new.friends[3] is None:
            new.lr_flip()
        self.board[y + 1, 0] = new
        s = self.s
        y += 1
        self.img[y * s: (y + 1) * s, 0: s] = new.core()


def identify_corners(tiles):
    corners = 1
    for i, tile in enumerate(tiles):
        for other in tiles[i + 1:]:
            tile.match(other)
    for tile in tiles:
        if tile.is_corner():
            corners *= tile.id
            if sum([tile.friends[i] is None for i in range(2)]) == 2:
                start = tile
    print(corners)
    return start


def assemble_puzzle(tiles, start):
    size = int(np.sqrt(tiles))
    board = Board(size, start)
    for y in range(size):
        for x in range(size - 1):
            board.insert_right(x, y)
        board.insert_down(y)
    return board.img


def hunt_monsters(ocean, monster):
    ym, xm = monster.shape
    xo, yo = ocean.shape
    monster_size = np.sum(monster)
    for tries in range(8):
        monster_count = 0
        ocean = flip_ocean(ocean, tries)
        for y in range(yo - ym + 1):
            for x in range(xo - xm + 1):
                patch = ocean[y: y + ym, x: x + xm]
                if np.sum(patch * monster) == monster_size:
                    monster_count += 1
        if monster_count != 0:
            return monster_count


def flip_ocean(ocean, i):
    if i == 4:
        return ocean.T
    else:
        return np.rot90(ocean)


def main():
    file = "input"
    if len(sys.argv) > 1:
        if sys.argv[1] == "test":
            file = "test"

    conv = {"#": 1, ".": 0, " ": -1}
    tiles = []
    for tile in open(file).read().strip().split("\n\n"):
        id, img = tile.split(":")
        id = int(id.split()[1])
        img = img.splitlines()[1:]
        img = np.asarray([[conv[p] for p in line] for line in img])
        tiles.append(Tile(id, img))

    monster = np.asarray([[conv[p] for p in line] for line in open("monster").read().splitlines()])
    monster = np.ma.masked_where(monster == -1, monster)

    s = identify_corners(tiles)
    ocean = assemble_puzzle(len(tiles), s)

    sea_monsters = hunt_monsters(ocean, monster)

    print(np.sum(ocean) - np.sum(monster) * sea_monsters)


if __name__ == "__main__":
    main()