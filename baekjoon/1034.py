import sys
from collections import defaultdict

def solution():
  input = sys.stdin.readline
  N, M = map(int, input().split())
  DB = defaultdict(int)
  for _ in range(N):
    lamp_str = input().rstrip()
    DB[lamp_str] += 1
  K = int(input())
  if K % 2 == 0:
    DB = [count for row, count in DB.items() if row.count("0")%2==0 and row.count("0")<=K]
  else:
    DB = [count for row, count in DB.items() if row.count("0")%2==1 and row.count("0")<=K]
  print(max(DB, default=0))
  
solution()