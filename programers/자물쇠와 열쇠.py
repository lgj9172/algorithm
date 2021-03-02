from copy import deepcopy
from collections import deque

# 90도만큼 시계방향으로 회전한 행렬을 얻습니다.
def get_rotate(matrix):
    size = len(matrix)
    new_matrix = [[0] * size for _ in range(size)]
    for i, row in enumerate(matrix):
        for j, data in enumerate(row):
            new_matrix[j][size - 1 - i] = data
    return new_matrix


def solution(key, lock):
    # 입력된 자물쇠 주변에 (key의 크기-1)만큼
    # 상하좌우에 padding을 삽입합니다.
    padding_size = len(key) - 1
    new_lock = deepcopy(lock)
    # 좌우에 padding 삽입
    new_lock = deque(
        [[0] * padding_size + row + [0] * padding_size for row in new_lock]
    )
    # 상하에 padding 삽입
    for _ in range(padding_size):
        new_lock.appendleft([0] * len(new_lock[0]))
        new_lock.append([0] * len(new_lock[0]))
    new_lock = list(new_lock)

    # 4번 회전하면서 확인
    for _ in range(4):
        # 왼쪽위 모서리부터 키를 이동하면서 확인
        for i in range(len(lock) + padding_size):
            for j in range(len(lock) + padding_size):
                # 키를 복사본에 덧셈
                current = deepcopy(new_lock)
                for a in range(len(key)):
                    for b in range(len(key)):
                        current[i + a][j + b] += key[a][b]
                focus = [
                    row[padding_size:-padding_size]
                    for row in current[padding_size:-padding_size]
                ]
                check = True
                # 덧셈 결과에 0이나 2가 있으면 실패, 1만 있으면 성공
                for a in range(len(focus)):
                    for b in range(len(focus)):
                        if focus[a][b] == 0 or focus[a][b] == 2:
                            check = False
                if check == True:
                    return True
        key = get_rotate(key)
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
