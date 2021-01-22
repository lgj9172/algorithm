N = int(input())
db = [[" " for _ in range(N)] for _ in range(N)]


def draw(x, y, n):
    if n == 1:
        db[x][y] = "*"
        return
    nn = n // 3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            draw(x + i * nn, y + j * nn, nn)


draw(0, 0, N)

for n in range(N):
    print("".join(db[n]))
