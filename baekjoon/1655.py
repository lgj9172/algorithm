import sys
import heapq


def solution():
  print, push, pop = sys.stdout.write, heapq.heappush, heapq.heappop
  N, *nums = map(int, sys.stdin.read().split())
  left_heap, right_heap = [], []
  count = 0
  for num in nums:
    push(left_heap, -num)
    if count % 2 == 0:  
      push(right_heap, -pop(left_heap))
      push(left_heap, -pop(right_heap))
    else:
      push(right_heap, -pop(left_heap))
    print(f'{-left_heap[0]}\n')
    count += 1
  
solution()