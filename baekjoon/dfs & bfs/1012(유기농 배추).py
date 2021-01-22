from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)

T = int(input())
answer = []

def dfs(db,i,j,count):
    if i < 0 or j < 0 or i > M-1 or j > N-1:
        return
    elif db[j][i] is False:
        return
    elif db[j][i] is True:
        db[j][i] = count
        dfs(db,i-1,j,count)
        dfs(db,i+1,j,count)
        dfs(db,i,j-1,count)
        dfs(db,i,j+1,count)

for _T in range(T):
    M, N, K = map(int, input().split())
    db = [[False]*M for _ in range(N)]
    count = 0
    for _K in range(K):
        A, B = map(int, input().split())
        db[B][A] = True
    for j in range(N):
        for i in range(M):
            if db[j][i] is True:
                count+=1
                dfs(db,i,j,count)
    answer.append(count)
for i in answer:
    print(i)