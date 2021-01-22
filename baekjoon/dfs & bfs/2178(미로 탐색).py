from collections import deque
N, M = map(int, input().split())
db = []
for _ in range(N):
    db.append(list(map(int,input())))
def bfs(i, j, count):
    history = []
    queue = deque([(i,j,count)])
    while queue:
        a, b, c = queue.popleft()
        if a < 0 or b < 0 or a > N-1 or b> M-1:
            continue
        elif db[a][b] == 0:
            continue
        elif (a, b) not in history:
            db[a][b] = c
            history.append((a, b))
            queue.append((a-1, b, c+1))
            queue.append((a+1, b, c+1))
            queue.append((a, b+1, c+1))
            queue.append((a, b-1, c+1))
bfs(0,0,1)
print(db[N-1][M-1])