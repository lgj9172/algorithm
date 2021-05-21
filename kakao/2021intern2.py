from collections import deque
from copy import deepcopy


def solution(places):
    answer = []
    for place in places:
        DB = [[e for e in row] for row in place]
        valid = True
        for x in range(5):
            for y in range(5):
                target = DB[x][y]
                if target == "P":
                    TEMPDB = deepcopy(DB)
                    queue = deque([(x, y, 0)])
                    while queue:
                        i, j, level = queue.pop()
                        if i < 0 or i > 4 or j < 0 or j > 4:
                            continue
                        if TEMPDB[i][j] == "P" and level > 0:
                            valid = False
                            break
                        if TEMPDB[i][j] == "X" or TEMPDB[i][j] == "*":
                            continue
                        TEMPDB[i][j] = "*"
                        if level < 2:
                            queue.append((i-1, j, level+1))
                            queue.append((i+1, j, level+1))
                            queue.append((i, j+1, level+1))
                            queue.append((i, j-1, level+1))
                if valid == False:
                    break
            if valid == False:
                break
        answer.append(1 if valid else 0)
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))