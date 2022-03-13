import sys
from heapq import heappop, heappush

def solution():
  input = sys.stdin.readline
  N = int(input())
  MAP = [list(map(int, input().split())) for _ in range(N)]
  for row in range(N):
    for col in range(N):
      if MAP[row][col] == 9:
        q = [(0, row, col)]
        MAP[row][col] = 0
        break
  visited = [[False]*N for _ in range(N)]
  shark_size, kill_count, answer = 2, 0, 0
  d = ((-1, 0), (1, 0), (0, -1), (0, 1))
  while q:
    time, row, col = heappop(q)
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
      q = [(time, row, col)]
      visited = [[False]*N for _ in range(N)]
      MAP[row][col] = 0
      answer = time
      kill_count += 1
      if(kill_count == shark_size):
        shark_size += 1
        kill_count = 0
      continue
    for dx, dy in d:
      heappush(q, (time+1, row+dx, col+dy))
  print(f'{answer}')
    
solution()