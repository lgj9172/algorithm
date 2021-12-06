import sys
from collections import deque


def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    HISTORY = [[False for _ in range(M)]for _ in range(N)]
    MELT_COUNT = 0
    while True:
        GLACIER_COUNT = 0
        for r in range(1, N-1):
            for c in range(1, M-1):
                value = MAP[r][c]
                if HISTORY[r][c] == True:
                    # 이미 진행한 곳 제외
                    continue
                elif HISTORY[r][c] == False and value == 0:
                    # 0이어서 진행 할 필요가 없는 곳은 제외
                    continue
                elif HISTORY[r][c] == False and value != 0:
                    # 진행이 필요한 곳
                    GLACIER_COUNT += 1
                    if GLACIER_COUNT >= 2:
                        print(MELT_COUNT)
                        return
                    queue = deque([(r, c)])
                    while queue:
                        i, j = queue.popleft()
                        # 해당 지역이 인덱스 범위를 넘어가는 곳이면 진행하지 않음
                        if i < 1 or i > N-2 or j < 1 or j > M-2:
                            continue
                        # 해당 지역이 이미 기록된 지역이면 진행하지 않음
                        if HISTORY[i][j] == True:
                            continue
                        # 해당 지역이 0인 지역이면 진행하지 않음
                        if MAP[i][j] == 0:
                            continue
                        HISTORY[i][j] = True
                        # 이 지역을 주변 0갯수만큼 제거해버립니다.
                        MAP[i][j] = max(MAP[i][j] - sum([
                            1 if MAP[i][j-1] == 0 and HISTORY[i][j -
                                                                 1] == False else 0,
                            1 if MAP[i][j+1] == 0 and HISTORY[i][j +
                                                                 1] == False else 0,
                            1 if MAP[i-1][j] == 0 and HISTORY[i -
                                                              1][j] == False else 0,
                            1 if MAP[i+1][j] == 0 and HISTORY[i +
                                                              1][j] == False else 0,
                        ]), 0)
                        # 상하좌우부분을 큐에 추가합니다.
                        queue.append((i, j-1))
                        queue.append((i, j+1))
                        queue.append((i-1, j))
                        queue.append((i+1, j))
        if GLACIER_COUNT == 1:
            MELT_COUNT += 1
            HISTORY = [[False for _ in range(M)]for _ in range(N)]
        elif GLACIER_COUNT == 0:
            print(0)
            return


solution()
