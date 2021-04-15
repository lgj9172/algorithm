import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline
N: int = int(input())
adj = defaultdict(list)
par = defaultdict(int)
for _ in range(N - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

queue = deque([(1, 1)])
history = set()
while queue:
    target, parent = queue.popleft()
    if target in history:
        continue
    history.add(target)
    par[target] = parent
    for n in adj[target]:
        queue.append((n, target))

for e in range(2, N+1):
    print(par[e])

