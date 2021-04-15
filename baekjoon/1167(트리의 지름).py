from copy import deepcopy
from sys import stdin
from collections import deque
from collections import defaultdict
readline = stdin.readline
V = int(readline())
graph = defaultdict(list)
for _ in range(V):
    line = tuple(map(int, readline().split()))
    start = 0
    for i, e in enumerate(line):
        if i == 0:
            start = e
        elif i == len(line)-1:
            break
        elif i % 2 == 1:
            graph[start].append((e, line[i+1]))
# stage1
history = set()
MAX = 0
MAX_TARGET = 0
queue = deque([(1, MAX)])
while queue:
    target, sumation = queue.popleft()
    if target in history:
        continue
    history.add(target)
    if MAX <= sumation:
        MAX = sumation
        MAX_TARGET = target
    for ntarget, cost in graph[target]:
        queue.append((ntarget, sumation+cost))
# stage2
history = set()
MAX = 0
queue = deque([(MAX_TARGET, MAX)])
while queue:
    target, sumation = queue.popleft()
    if target in history:
        continue
    history.add(target)
    if MAX <= sumation:
        MAX = sumation
    for ntarget, cost in graph[target]:
        queue.append((ntarget, sumation+cost))
print(MAX)