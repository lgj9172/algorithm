from copy import deepcopy
from pprint import pprint
from collections import defaultdict, deque

N, Q = map(int, input().split())  # 격자크기(2^N), 시전횟수
A = [list(map(int, input().split())) for _ in range(2 ** N)]  # 격자
L = list(map(int, input().split()))  # 시전시 격자크기(2^N)


def rotate_small_box(A, x, y, size):
    temp = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            temp[j][size - 1 - i] = A[x + i][y + j]
    for i in range(size):
        for j in range(size):
            A[x + i][y + j] = temp[i][j]


def rotate(A, l):
    small_box_size = 2 ** l  # 작은 격자의 크기
    iteration = int(len(A) / small_box_size)  # 작은 격자 가로 반복가능 횟수
    for i in range(iteration):
        for j in range(iteration):
            x = i * small_box_size
            y = j * small_box_size
            rotate_small_box(A, x, y, small_box_size)


def melt(A):
    NA = deepcopy(A)
    size = len(A)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(size):
        for j in range(size):
            count = 0
            for e in range(4):
                nx = i + dx[e]
                ny = j + dy[e]
                if 0 <= nx <= size - 1 and 0 <= ny <= size - 1 and A[nx][ny] > 0:
                    count += 1
            if count < 3 and A[i][j] > 0:
                NA[i][j] = A[i][j] - 1
    for i in range(size):
        for j in range(size):
            A[i][j] = NA[i][j]


for l in L:
    # 격자 쪼개서 돌리기
    rotate(A, l)
    # 각각의 칸 주변에 얼음이 3칸 이상 없으면 1줄이기
    melt(A)
SUM = 0
for row in A:
    SUM += sum(row)
print(SUM)

size = len(A)
map_index = 0
for i in range(size):
    for j in range(size):
        if A[i][j] > 0:
            map_index -= 1
            queue = deque()
            queue.append((i, j))
            while queue:
                x, y = queue.popleft()
                if x < 0 or x > size - 1 or y < 0 or y > size - 1:
                    continue
                if A[x][y] <= 0:
                    continue
                A[x][y] = map_index
                queue.append((x + 1, y))
                queue.append((x - 1, y))
                queue.append((x, y + 1))
                queue.append((x, y - 1))

counter = defaultdict(int)
counter[0] = 0
for row in A:
    for e in row:
        if e != 0:
            counter[e] += 1
MAX_COUNT = max(counter.values())
print(MAX_COUNT)