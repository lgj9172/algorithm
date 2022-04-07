import sys
from collections import deque

def solution():
  input = sys.stdin.readline
  MAP = [list(input().rstrip()) for _ in range(12)]
  answer = 0
  while True:
    poped = False
    for row in range(12):
      for col in range(6):
        char = MAP[row][col]
        if char == ".":
          continue
        else:
          history = set()
          q = deque([(row, col)])
          while q:
            crow, ccol = q.popleft()
            if not(0<=crow<12) or not(0<=ccol<6):
              continue
            if (crow, ccol) in history:
              continue
            if MAP[crow][ccol] != char:
              continue
            history.add((crow, ccol))
            for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
              q.append((crow+dx, ccol+dy))
          if len(history) >= 4:
            poped = True
            for crow, ccol in history:
              MAP[crow][ccol] = "."  
    for col in range(6):
      space_count = 0
      for row in reversed(range(12)):
        target = MAP[row][col]
        if target == ".":
          space_count += 1
        else:
          MAP[row][col] = "."
          MAP[row+space_count][col] = target
    if poped:
      answer += 1
    else:
      break
  print(answer)
  
solution()