import sys
from collections import defaultdict

input = sys.stdin.readline
N, M = map(int, input().split())
DB = defaultdict(set)
COUNT = [0] * (N+1)

for _ in range(M):
    start, end = map(int, input().split())
    DB[start].add(end)
    COUNT[end] += 1

ANSWER = []
queue = [i for i, e in enumerate(COUNT) if e == 0 and i != 0]
while queue:
    current = queue.pop()
    ANSWER.extend([current])
    nexts = DB[current]
    for next in nexts:
        COUNT[next] -= 1
        if COUNT[next] == 0:
            queue.append(next)

print(*ANSWER)
