import heapq


def solution(land, height):

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    n = len(land)
    visited = [[False] * n for x in range(n)]
    # 시작점은 0,0 말고 아무거나 해도 됨
    h = [(0, 0, 0)]
    res = 0
    while h:
        cnt, x, y = heapq.heappop(h)

        if visited[x][y]:
            continue

        res += cnt
        visited[x][y] = True
        for i in range(4):
            xx = dx[i] + x
            yy = dy[i] + y
            # 방문하지 않은 경우만 check
            if 0 <= xx < n and 0 <= yy < n and not visited[xx][yy]:
                temp = abs(land[x][y] - land[xx][yy])
                # height보다 차이가 크다면 그 차이를 넣어줘야함(사다리 건설비용)
                # height보다 작다면 사다리 건설비용이 들지 않기 때문에 0을 삽입
                if temp > height:
                    heapq.heappush(h, (temp, xx, yy))
                else:
                    heapq.heappush(h, (0, xx, yy))
    return res


print(
    solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3)
)  # 15