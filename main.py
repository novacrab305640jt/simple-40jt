"""
Simple 2D grid game: move '@' to 'X' avoiding '#'.
"""
import sys

GRID = [
    list("##########"),
    list("#        #"),
    list("#  ####  #"),
    list("#  #  #  #"),
    list("#  ####  #"),
    list("#        #"),
    list("##########"),
]

PLAYER = [1, 1]
TARGET = [5, 8]

MOVES = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}

def draw():
    for y, row in enumerate(GRID):
        line = ''
        for x, ch in enumerate(row):
            if [y, x] == PLAYER:
                line += '@'
            elif [y, x] == TARGET:
                line += 'X'
            else:
                line += ch
        print(line)

def move(key):
    if key not in MOVES:
        return
    dy, dx = MOVES[key]
    y, x = PLAYER[0] + dy, PLAYER[1] + dx
    if GRID[y][x] != '#':
        PLAYER[0], PLAYER[1] = y, x

def main():
    while True:
        draw()
        if PLAYER == TARGET:
            print("You win!")
            break
        key = input("Move (WASD): ").lower()
        move(key)
        print("\n" * 2)

if __name__ == "__main__":
    main()