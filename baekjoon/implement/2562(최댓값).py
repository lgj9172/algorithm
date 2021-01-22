numbers = [int(input()) for _ in range(9)]
INDEX, MAX = 0, 0
for index, number in enumerate(numbers):
    if number > MAX:
        INDEX = index
        MAX = number
print(MAX)
print(INDEX + 1)
