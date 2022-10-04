import heapq
import sys

def solution():
  sys.setrecursionlimit(10**9)
  sys.stdin.readline = input
  N, M = map(int, input().split())
  heap = []
  for _ in range(N):
    number = int(input())
    heapq.heappush(heap, (number, number))
  for _ in range(M-1):
    total_time, current_time = heapq.heappop(heap)
    heapq.heappush(heap, (total_time+current_time, current_time))
  print(heap[0][0]) 


solution()