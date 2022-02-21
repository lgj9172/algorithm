# import sys
# from bisect import bisect_left

# N = int(sys.stdin.readline())
# A = list(map(int, sys.stdin.readline().split()))
# DP = [0]

# for e in A:
#     if DP[-1] < e:
#         DP.append(e)
#     else:
#         index = bisect_left(DP, e)
#         DP[index] = e

# print(len(DP) - 1)


import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
DP = []

for e in A:
    index = bisect_left(DP, e)
    if len(DP) == index:
        DP.append(e)
    else:
        DP[index] = e

print(len(DP))
