N = int(input())
DB = [list(map(int, input().split())) for _ in range(N)]


def go_left(x, y, DB):
    a = DB[x][y - 1]
    DB[x - 2][y - 1] += int((DB[x][y - 1] * 0.02))
    a -= int((DB[x][y - 1] * 0.02))
    DB[x + 2][y - 1] += int((DB[x][y - 1] * 0.02))
    a -= int((DB[x][y - 1] * 0.02))

    DB[x - 1][y - 2] += int((DB[x][y - 1] * 0.1))
    a -= int((DB[x][y - 1] * 0.1))
    DB[x + 1][y - 2] += int((DB[x][y - 1] * 0.1))
    a -= int((DB[x][y - 1] * 0.1))

    DB[x - 1][y - 1] += int((DB[x][y - 1] * 0.07))
    a -= int((DB[x][y - 1] * 0.07))
    DB[x + 1][y - 1] += int((DB[x][y - 1] * 0.07))
    a -= int((DB[x][y - 1] * 0.07))

    DB[x - 1][y] += int((DB[x][y - 1] * 0.01))
    a -= int((DB[x][y - 1] * 0.01))
    DB[x + 1][y] += int((DB[x][y - 1] * 0.01))
    a -= int((DB[x][y - 1] * 0.01))

    DB[x][y - 3] += int((DB[x][y - 1] * 0.05))
    a -= int((DB[x][y - 1] * 0.05))

    DB[x][y - 2] += a
    DB[x][y - 1] = 0


def get_rotate_right(DB):
    size = len(DB)
    NDB = [[0 for _ in range(size)] for _ in range(size)]
    for r in range(size):
        for c in range(size):
            NDB[c][size - 1 - r] = DB[r][c]
    return NDB


NDB = [[0 for _ in range(len(DB) + 4)] for _ in range(len(DB) + 4)]
for i in range(len(DB)):
    for j in range(len(DB)):
        NDB[i + 2][j + 2] = DB[i][j]
DB = NDB

N = len(DB)
x, y = N // 2, N // 2
move = 1
while True:
    if x == 2:
        for _ in range(N - 5):
            go_left(x, y, DB)
            y -= 1
        break
    else:
        for _ in range(move):
            go_left(x, y, DB)
            y -= 1
        DB = get_rotate_right(DB)
        x, y = y, N - x - 1
        for _ in range(move):
            go_left(x, y, DB)
            y -= 1
        DB = get_rotate_right(DB)
        x, y = y, N - x - 1
        move += 1
        for _ in range(move):
            go_left(x, y, DB)
            y -= 1
        DB = get_rotate_right(DB)
        x, y = y, N - x - 1
        for _ in range(move):
            go_left(x, y, DB)
            y -= 1
        DB = get_rotate_right(DB)
        x, y = y, N - x - 1
        move += 1

out = 0
for i in range(len(DB)):
    for j in range(len(DB)):
        if i < 2 or i > len(DB) - 3 or j < 2 or j > len(DB) - 3:
            out += DB[i][j]
print(out)
