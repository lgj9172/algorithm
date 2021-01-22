from collections import deque
from collections import defaultdict

N = int(input())
V = int(input())
db = defaultdict(list)
for _ in range(V):
    A, B = map(int, input().split())
    db[A].append(B)
    db[B].append(A)
for key, value in db.items():
    db[key] = sorted(value)

def bfs():
    history = []
    queue = deque([1])
    while queue:
        n = queue.popleft()
        if n not in history:
            history.append(n)
            queue += db[n]
    return history

print(len(bfs())-1)