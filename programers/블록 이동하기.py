from collections import deque


def solution(board):
    queue = deque()
    queue.append([(0, 0.5), 0])  # 현재위치, 이동한기록, 이동횟수
    size = len(board)
    answer = 0
    history = set()
    while queue:
        target = queue.popleft()
        # 현재 위치가 좌표평면을 벗어나면 종료합니다.
        x, y = target[0]
        if x < 0 or y < 0 or x > size - 1 or y > size - 1:
            continue
        # 현재 위치가 물리적으로 갈 수 없는 곳(기계가 1과 걸쳐있으면)이면 종료합니다.
        if y % 1 == 0.5:  # 가로로 있을때
            if board[int(x)][int(y - 0.5)] == 1 or board[int(x)][int(y + 0.5)] == 1:
                continue
        elif x % 1 == 0.5:  # 세로로 있을때
            if board[int(x - 0.5)][int(y)] == 1 or board[int(x + 0.5)][int(y)] == 1:
                continue
        # 현재 위치가 이미 왔던 곳이라면 종료합니다.
        if (x, y) in history:
            continue
        # 현재 위치가 목적지라면 종료하고 이동 횟수를 반환하고 종료합니다.
        count = target[1]
        if (x, y) == (size - 1.5, size - 1) or (x, y) == (size - 1, size - 1.5):
            answer = count
            break
        # 상하좌우로 이동합니다.
        history.add((x, y))
        queue.append([(x - 1, y), count + 1])
        queue.append([(x + 1, y), count + 1])
        queue.append([(x, y - 1), count + 1])
        queue.append([(x, y + 1), count + 1])
        if y % 1 == 0.5:  # 가로로 있을때
            # 좌고정 위로 회전
            try:
                if board[int(x - 1)][int(y + 0.5)] == 0:
                    queue.append([(x - 0.5, y - 0.5), count + 1])
            except:
                pass
            # 좌고정 아래로 회전
            try:
                if board[int(x + 1)][int(y + 0.5)] == 0:
                    queue.append([(x + 0.5, y - 0.5), count + 1])
            except:
                pass
            # 우고정 위로 회전
            try:
                if board[int(x - 1)][int(y - 0.5)] == 0:
                    queue.append([(x - 0.5, y + 0.5), count + 1])
            except:
                pass
            # 우고정 아래로 회전
            try:
                if board[int(x + 1)][int(y - 0.5)] == 0:
                    queue.append([(x + 0.5, y + 0.5), count + 1])
            except:
                pass
        elif x % 1 == 0.5:  # 세로로 있을때
            # 위고정 왼쪽 회전
            try:
                if board[int(x + 0.5)][int(y - 1)] == 0:
                    queue.append([(x - 0.5, y - 0.5), count + 1])
            except:
                pass
            # 위고정 오른쪽 회전
            try:
                if board[int(x + 0.5)][int(y + 1)] == 0:
                    queue.append([(x - 0.5, y + 0.5), count + 1])
            except:
                pass
            # 아래고정 왼쪽 회전
            try:
                if board[int(x - 0.5)][int(y - 1)] == 0:
                    queue.append([(x + 0.5, y - 0.5), count + 1])
            except:
                pass
            # 아래고정 오른쪽 회전
            try:
                if board[int(x - 0.5)][int(y + 1)] == 0:
                    queue.append([(x + 0.5, y + 0.5), count + 1])
            except:
                pass

    return answer


# print(
#     solution(
#         [
#             [0, 0, 0, 1, 1],
#             [0, 0, 0, 1, 0],
#             [0, 1, 0, 1, 1],
#             [1, 1, 0, 0, 1],
#             [0, 0, 0, 0, 0],
#         ]
#     )
# )  # 7

# print(
#     solution(
#         [
#             [0, 0, 0, 0, 0, 0, 1],
#             [1, 1, 1, 1, 0, 0, 1],
#             [0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 1, 1, 1, 1, 0],
#             [0, 1, 1, 1, 1, 1, 0],
#             [0, 0, 0, 0, 0, 1, 1],
#             [0, 0, 1, 0, 0, 0, 0],
#         ]
#     )
# )  # 21

# print(
#     solution(
#         [
#             [0, 0, 0, 0, 0, 0, 1],
#             [1, 1, 1, 1, 0, 0, 1],
#             [0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 1, 1, 1, 0, 0],
#             [0, 1, 1, 1, 1, 1, 0],
#             [0, 0, 0, 0, 0, 1, 0],
#             [0, 0, 1, 0, 0, 0, 0],
#         ]
#     )
# )  # 11

# print(
#     solution(
#         [
#             [0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [1, 1, 1, 1, 1, 1, 1, 0, 0],
#             [1, 1, 1, 1, 1, 1, 1, 1, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 1, 1, 1, 1, 1, 0, 0],
#             [0, 1, 1, 1, 1, 1, 1, 1, 1],
#             [0, 0, 1, 1, 1, 1, 1, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [1, 1, 1, 1, 1, 1, 1, 1, 0],
#         ]
#     )
# )  # 33

# print(
#     solution(
#         [
#             [0, 0, 0, 0, 1, 0],
#             [0, 0, 1, 1, 1, 0],
#             [0, 1, 1, 1, 1, 0],
#             [0, 1, 0, 0, 1, 0],
#             [0, 0, 1, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0],
#         ]
#     )
# )  # 10

board = [[0] * 100 for _ in range(100)]
x = solution(board)
print(x)