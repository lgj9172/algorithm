# N * M 크기의 얼음틀
# 뚫려있는 부분은 0 칸막이는 1
# 두멍뚫려있는 부분끼리 서로 연결된 것으로 간주
# 첫번째 줄에 얼음 틀의 세로길이 N, 가로길이 M (1<=N, M<=1000)
# 두번째 줄부터 얼음 틀의 형태가 N개 주어짐
# 한번에 만들 수 있는 아이스크림의 개수?

# n, m = map(int, input().split())

# # 2차원 리스트의 맵 정보 입력 받기
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))

# 예제 입력
n, m = 4, 5,
graph = [
    [0,0,1,1,0]
    ,[0,0,0,1,1]
    ,[1,1,1,1,1]
    ,[0,0,0,0,0]
]

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y>=m:
        return False
    # 현재 노드를 아직 방문하지 않았으면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

# 모든 노드에 대해 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)