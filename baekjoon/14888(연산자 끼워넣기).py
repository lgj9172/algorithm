from itertools import permutations

N = int(input())
A = [e for e in map(int, input().split())]
O = [e for e in map(int, input().split())]
OS = (
    ["+" for _ in range(O[0])]
    + ["-" for _ in range(O[1])]
    + ["*" for _ in range(O[2])]
    + ["/" for _ in range(O[3])]
)
MIN = float("inf")
MAX = -float("inf")
for operand_list in set(permutations(OS)):
    result = A[0]
    for operand_index in range(N - 1):
        operand = operand_list[operand_index]
        next = A[operand_index + 1]
        if operand == "+":
            result += next
        elif operand == "-":
            result -= next
        elif operand == "*":
            result *= next
        elif operand == "/":
            if result < 0:
                result = -(-(result) // next)
            else:
                result //= next
    MIN = min(MIN, result)
    MAX = max(MAX, result)
print(MAX)
print(MIN)