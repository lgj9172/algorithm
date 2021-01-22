import itertools

# TEST1 = "3 3"
# TEST2 = "1231 1232 1233"
# N, M = map(int, TEST1.split())
# L = list(set(map(int, TEST2.split())))
N, M = map(int, input().split())
L = list(set(map(int, input().split())))
L.sort()
L = list(map(str, L))
answers = itertools.product(L, repeat=M)
for answer in answers:
    print(" ".join(answer))