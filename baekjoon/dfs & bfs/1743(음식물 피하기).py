from collections import deque
N, M, K = map(int, input().split())
positions = set()
for _ in range(K):
    x, y = map(int, input().split())
    positions.add((x, y))
max_count = 0
history = set()
for position in positions:
    count = 0
    queue = deque([position])
    while queue:
        target = queue.popleft()
        x, y = target
        if target in positions and target not in history:
            history.add(target)
            count += 1
            queue.extend([(x-1, y), (x+1, y), (x, y-1), (x, y+1)])
    max_count = max(max_count, count)
print(max_count)