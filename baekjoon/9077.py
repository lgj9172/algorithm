# import sys
#
# input = sys.stdin.readline
# T = int(input())
# ANSWER = []
# for _ in range(T):
#     N = int(input())
#     MAP = [[0 for _ in range(10001)] for _ in range(10001)]
#     MAX = 0
#     for _ in range(N):
#         X, Y = map(int, input().split())
#         minX, maxX = max(0, X-5), min(10000, X+5)
#         minY, maxY = max(0, Y-5), min(10000, Y+5)
#         for x in range(minX, maxX+1):
#             for y in range(minY, maxY+1):
#                 MAP[x][y] = MAP[x][y] + 1
#                 MAX = max(MAX, MAP[x][y])
#     ANSWER.append(MAX)
# for e in ANSWER:
#     print(e)


# import sys
# from collections import defaultdict

# input = sys.stdin.readline
# T = int(input())
# ANSWER = []
# for _ in range(T):
#     N = int(input())
#     MAP = defaultdict(int)
#     for _ in range(N):
#         X, Y = map(int, input().split())
#         MAP[(X, Y)] = 1
#     MAX = 0
#     for loc in list(MAP.keys()):
#         X, Y = loc
#         for dx, dy in [(-10, -10), (-10, 0), (0, -10), (0, 0)]:
#             x1, x2 = X + dx, X + dx + 12
#             y1, y2 = Y + dy, Y + dy + 12
#             COUNT = 0
#             for x in range(x1, x2):
#                 for y in range(y1, y2):
#                     COUNT += MAP[(x, y)]
#             MAX = max(MAX, COUNT)
#     ANSWER.append(MAX)
#     del(MAP)
# for e in ANSWER:
#     print(e)


import sys
from collections import defaultdict

input = sys.stdin.readline
T = int(input())
ANSWER = []
for _ in range(T):
    N = int(input())
    MAP = set()
    for _ in range(N):
        X, Y = map(int, input().split())
        MAP.add((X, Y))
    MAX_COUNT = 0
    for X, Y in MAP:
        target = [(x1, Y) for x1 in range(X-10, X+1)] + [(X, y1)
                                                         for y1 in range(Y-10, Y+1)]
        for x1, y1 in target:
            COUNT = 0
            for x in range(x1, x1+11):
                for y in range(y1, y1+11):
                    if (x, y) in MAP:
                        COUNT += 1
            MAX_COUNT = max(MAX_COUNT, COUNT)
    ANSWER.append(MAX_COUNT)
for e in ANSWER:
    print(e)
