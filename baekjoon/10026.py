import sys
from collections import deque


@profile
def solution():
    input = sys.stdin.readline
    N = int(input())
    picture = [list(input()) for _ in range(N)]
    history_normal = [[False for _ in range(N)] for _ in range(N)]
    history_blindness = [[False for _ in range(N)] for _ in range(N)]
    count_normal = 0
    count_blindness = 0
    for r in range(N):
        for c in range(N):
            queue = deque()
            color = picture[r][c]
            if history_normal[r][c] == False:
                count_normal += 1
                queue.extend([(r, c, "normal")])
            if history_blindness[r][c] == False:
                count_blindness += 1
                queue.extend([(r, c, "blindness")])
            while queue:
                row, col, typ = queue.popleft()
                if row < 0 or row >= N or col < 0 or col >= N:
                    continue
                if typ == "normal":
                    if history_normal[row][col] == True or color != picture[row][col]:
                        continue
                    history_normal[row][col] = True
                    queue.extend([(row, col-1, "normal"), (row, col+1, "normal"),
                                 (row-1, col, "normal"), (row+1, col, "normal")])
                else:
                    if history_blindness[row][col] == False and (color == picture[row][col] or (color in ["R", "G"] and picture[row][col] in ["R", "G"])):
                        pass
                    else:
                        continue
                    history_blindness[row][col] = True
                    queue.extend([(row, col-1, "blindness"), (row, col+1, "blindness"),
                                 (row-1, col, "blindness"), (row+1, col, "blindness")])
    print(count_normal, count_blindness)


solution()
