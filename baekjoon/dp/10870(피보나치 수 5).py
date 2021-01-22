n = int(input())
dp = []
for e in range(n + 1):
    if e == 0:
        dp.append(0)
    elif e == 1:
        dp.append(1)
    elif e == 2:
        dp.append(1)
    else:
        dp.append(dp[-1] + dp[-2])
print(dp[n])