N = int(input())
A = set(map(int, input().split()))
M = int(input())
B = map(int, input().split())

for target in B:
    if target in A:
        print(1)
    else:
        print(0)