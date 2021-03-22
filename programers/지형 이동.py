import math
from collections import deque, defaultdict
import sys

sys.setrecursionlimit(10 ** 6)


def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    elif a < b:
        parent[b] = a


def solution(land, height):
    size = len(land)
    history = [[0 for _ in range(size)] for _ in range(size)]  # 그룹 번호 저장
    ladder = defaultdict(lambda: math.inf)  # 그룹간의 최소비용 저장
    gr_num = 0
    for a in range(size):
        for b in range(size):
            if history[a][b] != 0:
                continue
            elif history[a][b] == 0:
                gr_num += 1
                queue = deque()
                queue.append((a, b))
                while queue:
                    x, y = queue.popleft()
                    target = land[x][y]
                    if not (0 <= x <= size - 1 and 0 <= y <= size - 1):
                        continue
                    if history[x][y] != 0:
                        continue
                    history[x][y] = gr_num
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx <= size - 1 and 0 <= ny <= size - 1:
                            next_target = land[nx][ny]
                            gap = abs(next_target - target)
                            ngr_num = history[nx][ny]
                            if ngr_num != 0 and ngr_num != gr_num:
                                ladder[tuple(sorted((gr_num, ngr_num)))] = min(
                                    ladder[tuple(sorted((gr_num, ngr_num)))], gap
                                )
                            elif gap <= height:
                                queue.append((nx, ny))

    answer = 0
    ladder = sorted(ladder.items(), key=lambda x: x[1])
    parent = {i: i for i in range(1, gr_num + 1)}
    for (x, y), cost in ladder:
        if find_parent(parent, x) != find_parent(parent, y):
            union_parent(parent, x, y)
            answer += cost
        if len(parent.values()) == 1:
            break

    return answer


print(
    solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3)
)  # 15
print(
    solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 1)
)  # 18
print(solution([[0, 1, 2, 3], [7, 6, 5, 4], [8, 9, 10, 11], [15, 14, 13, 12]], 1))  # 0
print(
    solution(
        [
            [1, 1, 5, 5],
            [10, 10, 50, 50],
            [100, 100, 500, 500],
            [1000, 1000, 5000, 5000],
        ],
        1,
    )
)  # 5443

print(
    solution(
        [
            [10, 10, 10, 10],
            [1, 30, 5, 10],
            [1, 20, 6, 10],
            [1, 1, 1, 1],
        ],
        3,
    )
)  # 4
