MAP = [[0 for _ in range(4)] for _ in range(4)]
DIR = [[0 for _ in range(4)] for _ in range(4)]
for r in range(4):
    l = list(map(int, input().split()))
    MAP[r][0], MAP[r][1], MAP[r][2], MAP[r][3] = l[0], l[2], l[4], l[6]
    DIR[r][0], DIR[r][1], DIR[r][2], DIR[r][3] = l[1], l[3], l[5], l[7]