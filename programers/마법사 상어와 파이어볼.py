# 격자크기, 파이어볼갯수, 이동횟수
N, M, K = map(int, input().split())
# (질량, 속력, 방향, 완료여부) 리스트가 들어있는 맵
MAP = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    # (좌표1, 좌표2, 질량, 속력, 방향(0~7))
    r, c, m, s, d = map(int, input().split())
    MAP[r - 1][c - 1].append((m, s, d, False))


def get_next_address(r, c, s, d):
    direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    nr = (r + s * direction[d][0]) % N
    nc = (c + s * direction[d][1]) % N
    return nr, nc


for _ in range(K):
    # 이동단계
    for r in range(N):
        for c in range(N):
            balls = MAP[r][c]
            nballs = []
            for ball in balls:
                m, s, d, done = ball
                if done == False:
                    nr, nc = get_next_address(r, c, s, d)
                    MAP[nr][nc].append((m, s, d, True))
                elif done == True:
                    nballs.append((m, s, d, True))
            MAP[r][c] = nballs
    # 합산 및 나누기단계
    for r in range(N):
        for c in range(N):
            balls = MAP[r][c]
            if len(balls) >= 2:
                count, nm, ns, nd = 0, 0, 0, set()
                for ball in balls:
                    m, s, d, done = ball
                    count += 1
                    nm += m
                    ns += s
                    nd.add(d % 2)
                nm = int(nm / 5)
                ns = int(ns / count)
                if len(nd) == 1:
                    MAP[r][c] = [(nm, ns, d, False) for d in range(0, 7, 2)]
                elif len(nd) == 2:
                    MAP[r][c] = [(nm, ns, d, False) for d in range(1, 8, 2)]
    # 정리 단계
    for r in range(N):
        for c in range(N):
            balls = MAP[r][c]
            nballs = []
            for ball in balls:
                m, s, d, done = ball
                if m > 0:
                    nballs.append((m, s, d, False))
            MAP[r][c] = nballs
SUM = 0
for row in MAP:
    for balls in row:
        for ball in balls:
            SUM += ball[0]
print(SUM)
