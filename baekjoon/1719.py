import sys

def solution():
  input = sys.stdin.readline
  N, M = map(int, input().split())
  MAP_COST = [[0 if A==B else float("inf") for B in range(N+1) ] for A in range(N+1)]
  MAP_FIRS = [["-" if A==B else 0 for B in range(N+1)] for A in range(N+1)]
  for _ in range(M):
    A, B, T = map(int, input().split())
    MAP_COST[A][B] = T
    MAP_COST[B][A] = T
    MAP_FIRS[A][B] = B
    MAP_FIRS[B][A] = A
  for MID in range(1, N+1):
    for STR in range(1, N+1):
      for FIN in range(1, N+1):
        cost1 = MAP_COST[STR][FIN]
        cost2 = MAP_COST[STR][MID] + MAP_COST[MID][FIN]
        if cost1 > cost2:
          MAP_COST[STR][FIN] = cost2
          MAP_FIRS[STR][FIN] = MAP_FIRS[STR][MID]
  for row in range(1, N+1):
    print(*MAP_FIRS[row][1:])
    
solution()