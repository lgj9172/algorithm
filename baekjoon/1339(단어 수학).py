from collections import defaultdict

N = int(input())

counter = defaultdict(int)

for _ in range(N):
    word = input()
    for i, c in enumerate(word):
        counter[c] += 10 ** (len(word) - i - 1)

answer = 0
start = 9
for count in sorted(counter.values(), reverse=True):
    answer += count * start
    start -= 1

print(answer)