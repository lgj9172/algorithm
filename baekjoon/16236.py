import sys
from collections import deque

def solution():
  input = sys.stdin.readline
  N = int(input())
  MAP = [list(map(int, input().split())) for _ in range(N)]
  x, y = 0, 0
  for row in range(N):
    for col in range(N):
      if MAP[row][col] == 9:
        x, y = row, col
        MAP[row][col] = 0
  q = deque([(x, y, 0)]) # (row, col, time)
  visited = [[False for _ in range(N)] for _ in range(N)]
  shark_size = 2
  kill_count = 0
  answer = 0
  while q:
    row, col, time = q.popleft()
    if not(0<=row<N) or not(0<=col<N):
      continue
    fish_size = MAP[row][col]
    if visited[row][col] == True:
      continue
    elif fish_size > shark_size:
      continue
    else:
      visited[row][col] = True
    if 0 < fish_size < shark_size:
      q = deque([(row, col, time)])
      visited = [[False for _ in range(N)] for _ in range(N)]
      MAP[row][col] = 0
      answer = time
      kill_count += 1
      if(kill_count == shark_size):
        shark_size += 1
        kill_count = 0
      continue
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      q.append((row+dx, col+dy, time+1))
    q = deque(sorted(q, key=lambda e:(e[2], e[0], e[1])))
  print(answer)
    
solution()