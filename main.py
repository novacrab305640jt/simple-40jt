"""
Simple 2D grid game: move a player across a 5x5 board.
"""

WIDTH, HEIGHT = 5, 5
OBSTACLES = {(2, 2)}
PLAYER_POS = [0, 0]

def display():
    for y in range(HEIGHT):
        row = ''
        for x in range(WIDTH):
            if [x, y] == PLAYER_POS:
                row += 'P'
            elif (x, y) in OBSTACLES:
                row += '#'
            else:
                row += '.'
        print(row)

def move(cmd):
    dirs = {'w': (0, -1), 's': (0, 1), 'a': (-1, 0), 'd': (1, 0)}
    if cmd not in dirs:
        return False
    dx, dy = dirs[cmd]
    nx, ny = PLAYER_POS[0] + dx, PLAYER_POS[1] + dy
    if 0 <= nx < WIDTH and 0 <= ny < HEIGHT and (nx, ny) not in OBSTACLES:
        PLAYER_POS[0], PLAYER_POS[1] = nx, ny
        return True
    return False

def main():
    while True:
        display()
        cmd = input("Move (w/a/s/d) or q to quit: ").strip().lower()
        if cmd == 'q':
            print("Goodbye!")
            break
        if not move(cmd):
            print("Can't move there!")

if __name__ == "__main__":
    main()