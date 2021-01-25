from collections import deque

N = int(input())
max_height = 0
min_height = 999
db = []
for _ in range(N):
    l = list(map(int, input().split()))
    max_height = max(max_height, *l)
    min_height = min(min_height, *l)
    db.append(l)
if max_height == min_height:
    print(1)
    exit()

result = 0
for water_height in range(min_height, max_height):
    map = [[e if e > water_height else 0 for e in line] for line in db]
    history = set()
    count = 0
    for i in range(N):
        for j in range(N):
            target = map[i][j]
            if target > 0 and (i, j) not in history:
                count += 1
                queue = deque([(i, j)])
                while queue:
                    ti, tj = queue.popleft()
                    if 0 <= ti <= N - 1 and 0 <= tj <= N - 1:
                        ctarget = map[ti][tj]
                        if ctarget > 0 and (ti, tj) not in history:
                            history.add((ti, tj))
                            queue.append((ti + 1, tj))
                            queue.append((ti - 1, tj))
                            queue.append((ti, tj + 1))
                            queue.append((ti, tj - 1))
    result = max(result, count)
print(result)