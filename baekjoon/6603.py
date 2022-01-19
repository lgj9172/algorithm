import sys
from itertools import combinations

input = sys.stdin.readline

while True:
    input_array = list(map(int, input().split()))
    K, S = input_array[0], input_array[1:]
    if K == 0:
        break
    else:
        C = combinations(S, 6)
        for c in C:
            print(*c)
        print("")
