from collections import defaultdict

N = int(input())
db = []
for _ in range(N):
    db.append(list(input()))

def dfs(i, j, count):
    if i < 0 or j < 0 or i > N-1 or j > N-1:
        return
    elif db[i][j] == "0":
        return
    elif db[i][j] == "1":
        db[i][j] = count
        counter[count] += 1
        dfs(i-1, j, count)
        dfs(i+1, j, count)
        dfs(i, j-1, count)
        dfs(i, j+1, count)

count = 0
counter = defaultdict(int)
for i in range(N):
    for j in range(N):
        n = db[i][j]
        if n == "1":
            count += 1
            dfs(i, j, count)

list_counter = []
for i in range(1, count+1):
    list_counter.append(counter[i])
list_counter.sort()

print(count)
for e in list_counter:
    print(e)