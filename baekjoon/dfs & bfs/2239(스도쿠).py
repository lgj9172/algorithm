# import time
# from collections import deque
# db = [[ int(e) for e in input() ] for _ in range(9)]
# targets = [(i,j) for i in range(9) for j in range(9) if db[i][j] == 0]
# while targets:
#     target = targets.popleft()
#     i, j = target
#     cand_set = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
#     cand_set = cand_set - set(db[i]) # 해당 좌표의 가로를 모두 제거
#     cand_set = cand_set - set([db[_][j] for _ in range(9)]) # 해당 좌표의 세로를 모두 제거
#     x, y = j//3, i//3 # 사분면 계산
#     cand_set = cand_set - set([db[Y][X] for X in range(x*3, x*3+3) for Y in range(y*3, y*3+3)]) # 해당 좌표의 사분면을 모두 제거
#     if len(cand_set)==1:
#         db[i][j] = cand_set.pop()
#     else:
#         targets.append(target)
# for _ in range(9):
#     print("".join(list(map(str, db[_]))))
import sys
from collections import deque

db = [[int(e) for e in str(sys.stdin.readline())[:9]] for _ in range(9)]  # 데이터베이스


def get_candidate(db, i, j):
    cand_set = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    cand_set = cand_set - set(db[i])  # 해당 좌표의 가로를 모두 제거
    cand_set = cand_set - set([db[_][j] for _ in range(9)])  # 해당 좌표의 세로를 모두 제거
    x, y = j // 3, i // 3  # 사분면 계산
    cand_set = cand_set - set(
        [db[Y][X] for X in range(x * 3, x * 3 + 3) for Y in range(y * 3, y * 3 + 3)]
    )  # 해당 좌표의 사분면을 모두 제거
    return sorted(list(cand_set))


# 현재 스도쿠에서 빈 위치를 찾습니다.
def find_next(db):
    for i in range(0, 9):
        for j in range(0, 9):
            if db[i][j] == 0:
                return i, j
    return -1, -1


# 빈 위치를 채웁니다.
def dfs(db, i=0, j=0):
    # 더 이상 채울 위치가 없이 완료하였을때 완료처리
    i, j = find_next(db)
    if i == -1:
        return True
    # 빈자리에 입력 가능한 원소들을 넣어보고 잘 되는지 확인
    for e in get_candidate(db, i, j):
        db[i][j] = e
        if dfs(db, i, j):
            return True
        db[i][j] = 0
    return False


dfs(db)
for e in range(9):
    sys.stdout.write("".join(list(map(str, db[e]))) + "\n")
