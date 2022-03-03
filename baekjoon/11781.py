import sys
from collections import defaultdict, deque

def get_arrival_time(departure_time, length, late, rush_hour_start, rush_hour_end):
  if late == 1:
    spend_time = 0
    distance = 0
    while distance != length:
      distance += 0.5
      current_time = departure_time + spend_time
      if rush_hour_start <= current_time < rush_hour_end:
        spend_time += 1
      else:
        spend_time += 0.5
    return departure_time + spend_time
  else:
    return departure_time + length
  

def solution():
  # input
  N, M, S, E = map(int, sys.stdin.readline().split())
  result = [1000000001] * (N+1)
  count = 0
  road = defaultdict(list) # (A) = (B, L, t1), (B) = (A, L, t2)
  for _ in range(M):
    A, B, L, t1, t2 = map(int, sys.stdin.readline().split())
    road[A].append((B, L, t1))
    road[B].append((A, L, t2))
  
  # bfs
  q = deque([(1, 0)]) # (currentNode, currentTime)
  while q:
    cnode_num, ctime = q.popleft()
    if ctime < result[cnode_num]: # 이전기록보다 더 빠를경우
      result[cnode_num] = ctime
    else:
      continue
    nnodes = road[cnode_num]
    for nnode in nnodes:
      nnode_num, length, late = nnode
      arrival_time = get_arrival_time(ctime, length, late, S, E)
      q.append((nnode_num, arrival_time))
  
  # result
  print(max(result[1:]))

solution()

# print(get_arrival_time(0, 8, 1, 4, 13))