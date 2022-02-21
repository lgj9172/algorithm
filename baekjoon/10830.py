import sys


def matrix_multiply(A, B, size):
    result = [[0 for _ in range(size)]for _ in range(size)]
    for row in range(size):
        for col in range(size):
            element = 0
            for idx in range(size):
                element += A[row][idx] % 1000 * B[idx][col] % 1000
            result[row][col] = element % 1000
    return result


N, B = map(int, sys.stdin.readline().split())
MATRIX = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ANSWER = [[1 if row == col else 0 for col in range(N)]for row in range(N)]

while True:
    if B == 1:
        ANSWER = matrix_multiply(ANSWER, MATRIX, N)
        break
    elif B % 2 == 0:
        B //= 2
        MATRIX = matrix_multiply(MATRIX, MATRIX, N)
    else:
        B -= 1
        ANSWER = matrix_multiply(ANSWER, MATRIX, N)

for row in ANSWER:
    print(*row)
