from collections import defaultdict
from collections import deque
N, M, V = map(int, input().split())
db = defaultdict(list)
for _ in range(M):
    A, B = map(int, input().split())
    db[A].append(B)
    db[A].sort()
    db[B].append(A)
    db[B].sort()
# dfs
def dfs():
    history = []
    stack = [V]
    while stack:
        n = stack.pop()
        if n not in history:
            history.append(n)
            stack += reversed(db[n])
    return history
# bfs
def bfs():
    history = []
    queue = deque([V])
    while queue:
        n = queue.popleft()
        if n not in history:
            history.append(n)
            queue += db[n]
    return history
result1 = dfs()
result2 = bfs()
print(" ".join(map(str, result1)))
print(" ".join(map(str, result2)))