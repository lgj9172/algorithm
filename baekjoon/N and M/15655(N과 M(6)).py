import itertools

# TEST1 = "4 2"
# TEST2 = "9 8 7 1"
# N, M = map(int, TEST1.split())
# L = list(set(map(int, TEST2.split())))
N, M = map(int, input().split())
L = list(set(map(int, input().split())))
L.sort()

answers = itertools.combinations(L, M)
for answer in answers:
    print(" ".join(list(map(str, answer))))