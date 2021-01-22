from collections import deque
M, N = map(int, input().split())
db = []
for _ in range(N):
    db.append(list(map(int, input().split())))
start = []
for i in range(N):
    for j in range(M):
        if db[i][j] == 1:
            db[i][j] = 0
            start.append((i,j,0))
count = 0
def bfs():
    # history = []
    queue = deque(start)
    while queue:
        i, j, c = queue.popleft()
        if i < 0 or j < 0 or i > N-1 or j > M-1:
            continue
        elif db[i][j] == -1 or db[i][j] == 1:
            continue
        elif db[i][j] == 0:
            # history.append(i, j)
            db[i][j] = 1
            global count
            count = c
            queue.append((i-1,j,c+1))
            queue.append((i+1,j,c+1))
            queue.append((i,j-1,c+1))
            queue.append((i,j+1,c+1))
bfs()
mature = True
for i in range(len(db)):
    if 0 in db[i]:
        mature = False
        break
if mature is False:
    print(-1)
else:
    print(count)