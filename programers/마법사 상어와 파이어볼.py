N, M, K = map(int, input().split())  # 격자크기,
l = []
for _ in range(M):
    r, c, m, s, d = list(map(int, input().split()))
    l.append((r, c, m, s, d))
