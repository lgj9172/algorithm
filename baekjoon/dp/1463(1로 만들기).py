X = int(input())
dp = []
for x in range(X + 1):
    if x == 0:
        dp.append(0)
    elif x == 1:
        dp.append(0)
    elif x == 2:
        dp.append(1)
    elif x == 3:
        dp.append(1)
    else:
        candidate = []
        if x % 3 == 0:
            candidate.append(dp[x // 3] + 1)
        if x % 2 == 0:
            candidate.append(dp[x // 2] + 1)
        candidate.append(dp[x - 1] + 1)
        dp.append(min(candidate))
print(dp[X])