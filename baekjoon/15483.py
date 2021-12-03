import sys

cstr = input()
nstr = input()
cstr_len = len(cstr)
nstr_len = len(nstr)

DP = [[0 for _ in range(nstr_len+1)] for _ in range(cstr_len+1)]
DP[0][0] = 0
for e in range(1, cstr_len+1):
    DP[e][0] = e
for e in range(1, nstr_len+1):
    DP[0][e] = e

for row in range(1, cstr_len+1):
    for col in range(1, nstr_len+1):
        if cstr[row-1] == nstr[col-1]:
            DP[row][col] = DP[row-1][col-1]
        else:
            DP[row][col] = min(DP[row][col-1], DP[row-1]
                               [col-1], DP[row-1][col]) + 1

print(DP[cstr_len][nstr_len])
