from sys import stdin
from collections import deque


def solution():
    # input
    input = stdin.readline
    m, n = map(int, input().split())
    k = int(input())
    BUS = [0] * (k+1)  # 모든 버스 정보
    for _ in range(k):
        b, x1, y1, x2, y2 = map(int, input().split())
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        BUS[b] = (x1, y1, x2, y2)
    sx, sy, dx, dy = map(int, input().split())

    # bfs
    visited = [0] * (k+1)
    queue = deque()
    for i in range(1, k+1):
        if BUS[i][0] <= sx <= BUS[i][2] and BUS[i][1] <= sy <= BUS[i][3]:
            queue.append(i)
            visited[i] = 1
    answer = 0
    while queue:
        bnum = queue.popleft()
        if BUS[bnum][0] <= dx <= BUS[bnum][2] and BUS[bnum][1] <= dy <= BUS[bnum][3]:
            answer = visited[bnum]
            break
        for nbnum in range(1, k+1):
            if not visited[nbnum]:
                if BUS[bnum][0] <= BUS[nbnum][2] and BUS[bnum][2] >= BUS[nbnum][0] and BUS[bnum][1] <= BUS[nbnum][3] and BUS[bnum][3] >= BUS[nbnum][1]:
                    visited[nbnum] = visited[bnum] + 1
                    queue.append(nbnum)
    print(answer)


solution()


# # analysis
# TRANSFER = defaultdict(set)  # 버스노선별 환승 가능 버스노선
# START_BUS = set()  # 시작 지점의 버스 노선
# FINISH_BUS = set()  # 종료 지점의 버스 노선
# for sbus_number, sx1, sy1, sx2, sy2 in BUS:
#     for fbus_number, fx1, fy1, fx2, fy2 in BUS:
#         if sbus_number == fbus_number:
#             continue
#         # row to row
#         elif sy1 == sy2 and fy1 == fy2 and sy1 == fy1:
#             if sx2 >= fx1 and sx1 <= fx2:
#                 TRANSFER[sbus_number].add(fbus_number)
#                 TRANSFER[fbus_number].add(sbus_number)
#         # row to col
#         elif sy1 == sy2 and fx1 == fx2:
#             if sx1 <= fx1 <= sx2 and fy1 <= sy1 <= fy2:
#                 TRANSFER[sbus_number].add(fbus_number)
#                 TRANSFER[fbus_number].add(sbus_number)
#         # col to col
#         elif sx1 == sx2 and fx1 == fx2 and sx1 == fx1:
#             if sy2 >= fy1 and sy1 <= fy2:
#                 TRANSFER[sbus_number].add(fbus_number)
#                 TRANSFER[fbus_number].add(sbus_number)
#         # col to row
#         # elif sx1 == sx2 and fy1 == fy2:
#         else:
#             if sy1 <= fy1 <= sy2 and fx1 <= sx1 <= fx2:
#                 TRANSFER[sbus_number].add(fbus_number)
#                 TRANSFER[fbus_number].add(sbus_number)
#     if sy1 == sy2:  # row
#         if sy1 == sy and sx1 <= sx <= sx2:  # start
#             START_BUS.add(sbus_number)
#         if sy1 == dy and sx1 <= dx <= sx2:  # finish
#             FINISH_BUS.add(sbus_number)
#     else:  # col
#         if sx1 == sx and sy1 <= sy <= sy2:  # start
#             START_BUS.add(sbus_number)
#         if sx1 == dx and sy1 <= dy <= sy2:  # finish
#             FINISH_BUS.add(sbus_number)

# bfs
# answer = math.inf
# start_list = []
# for start_bus_number in START_BUS:
#     start_list.append((start_bus_number, set()))  # 현재 버스 번호, history
# queue = deque(start_list)
# while queue:
#     current_bus_number, history = queue.popleft()
#     if current_bus_number in history:
#         continue
#     if len(history)+1 >= answer:
#         continue
#     if current_bus_number in FINISH_BUS:
#         answer = min(answer, len(history)+1)
#     next_bus_numbers = TRANSFER[current_bus_number]
#     for next_bus_number in next_bus_numbers:
#         queue.append((next_bus_number, history.union({current_bus_number})))

print(answer)
