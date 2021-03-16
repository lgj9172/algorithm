from collections import deque
from copy import deepcopy


def solution(board):
    db = deepcopy(board)
    queue = deque([(0, 0, "none", 0)])  # x, y, vector, point
    size = len(db)
    while queue:
        x, y, vector, point = queue.popleft()
        if x < 0 or x > size - 1 or y < 0 or y > size - 1:
            continue
        if db[x][y] == 1:
            continue

        if db[x][y] == 0 or point <= db[x][y]:
            db[x][y] = point
        else:
            continue

        queue.append(
            (
                x + 1,
                y,
                "east",
                point + 100 if vector == "none" or vector == "east" else point + 600,
            )
        )
        queue.append(
            (
                x - 1,
                y,
                "west",
                point + 100 if vector == "none" or vector == "west" else point + 600,
            )
        )
        queue.append(
            (
                x,
                y + 1,
                "south",
                point + 100 if vector == "none" or vector == "south" else point + 600,
            )
        )
        queue.append(
            (
                x,
                y - 1,
                "north",
                point + 100 if vector == "none" or vector == "north" else point + 600,
            )
        )
    answer = db[-1][-1]
    return answer


print(
    solution(
        [
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
        ]
    )
)
