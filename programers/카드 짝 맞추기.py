from collections import deque


def get_control_offset(db, x, y):
    done = [False, False, False, False]
    up, down, left, right = 0, 0, 0, 0
    for i in range(1, 4):
        if (y - i >= 0 and int(db[x + y * 4 - i * 4]) != 0 and done[0] == False) or (
            y - i == 0 and done[0] == False
        ):
            up = i
            done[0] = True
        if (y + i <= 3 and int(db[x + y * 4 + i * 4]) != 0 and done[1] == False) or (
            y + i == 3 and done[1] == False
        ):
            down = i
            done[1] = True
        if (x - i >= 0 and int(db[x + y * 4 - i]) != 0 and done[2] == False) or (
            x - i == 0 and done[2] == False
        ):
            left = i
            done[2] = True
        if (x + i <= 3 and int(db[x + y * 4 + i]) != 0 and done[3] == False) or (
            x + i == 3 and done[3] == False
        ):
            right = i
            done[3] = True
    return up, down, left, right


def solution(board, r, c):
    # 엔터를 누르는 경우
    # history 작성을 위한 배열 문자열화
    db = "".join(["".join(map(str, row)) for row in board])
    # 보드판복사본, 현재x, 현재y, 이동카운트, 목표타겟
    queue = deque([(db, c, r, 0, -1)])
    history = set()

    while queue:
        db, cx, cy, count, number = queue.popleft()
        # 더 이상 카드가 없는 경우
        if db.count("0") == 16:
            return count
        # 현재 분석하려는 위치가 범위를 벗어나는 경우
        if cx < 0 or cx > 3 or cy < 0 or cy > 3:
            continue
        # 현재 분석하려는 위치가 이미 분석했던 위치인 경우
        if (db, cx, cy, number) in history:
            continue
        else:
            history.add((db, cx, cy, number))

        # 현재 분석하려는 위치에 카드가 있고, 목표가 없는 경우
        if int(db[cx + cy * 4]) != 0 and number == -1:
            temp = list(db)
            temp[cx + cy * 4] = "0"
            new_db = "".join(temp)
            queue.append((new_db, cx, cy, count + 1, int(db[cx + cy * 4])))
        # 현재 분석하려는 위치의 카드와 목표가 같은 경우
        elif int(db[cx + cy * 4]) == number:
            queue.append((db.replace(str(number), "0", -1), cx, cy, count + 1, -1))

        # 상하좌우로 이동
        queue.append((db, cx + 0, cy - 1, count + 1, number))
        queue.append((db, cx + 0, cy + 1, count + 1, number))
        queue.append((db, cx - 1, cy + 0, count + 1, number))
        queue.append((db, cx + 1, cy + 0, count + 1, number))
        # 컨트롤 누르고 상하좌우로 이동
        up, down, left, right = get_control_offset(db, cx, cy)
        queue.append((db, cx + 0, cy - up, count + 1, number))
        queue.append((db, cx + 0, cy + down, count + 1, number))
        queue.append((db, cx - left, cy + 0, count + 1, number))
        queue.append((db, cx + right, cy + 0, count + 1, number))


print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0))
print(solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1))
