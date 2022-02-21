import sys

input = sys.stdin.readline
N = int(input())
K = int(input())

start, end, result = 0, K, 0
while True:
    center = (start + end) // 2
    count = 0
    for row in range(1, N + 1):
        count += min(center // row, N)
    if count < K:
        start = center + 1
    else:
        result = center
        end = center - 1
    if start > end:
        break

print(result)
