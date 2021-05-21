# 문제 설명
# 1부터 n까지 번호가 하나씩 붙은 n개의 노드를 갖는 트리가 주어집니다. 각 노드에는 값이 하나씩 들어 있으며, 이 트리의 루트 노드는 1번 노드입니다. 당신은 이 트리에 대해 다음과 같은 쿼리 두 종류를 처리하면 됩니다.
#
# 1번 쿼리: 정수 u가 주어집니다. u번 노드의 서브 트리의 모든 노드의 값의 합을 구해야 합니다.
# 2번 쿼리: 정수 u, w가 주어집니다. u번 노드의 값을 삭제한 뒤, u번 노드의 부모 노드의 값을 u번 노드로 복사합니다., u번 노드의 부모 노드에 대해 같은 작업을 반복하며 루트노드까지 거슬러 올라갑니다. 마지막으로 루트 노드의 값을 w로 바꿉니다.
# 트리의 노드 초기값이 담긴 정수 배열 values, 트리의 연결 상태가 담긴 2차원 정수 배열 edges, 쿼리들이 담긴 2차원 정수 배열 queries가 주어집니다. 쿼리들을 순서대로 처리할 때, 각 1번 쿼리에 대한 답을 수행 순서대로 배열에 담아 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# 1 ≤ values의 길이 ≤ 100,000
# values의 길이는 트리의 노드 개수를 의미합니다.
# values[i]는 i+1번 노드의 초기 값을 의미합니다.
# edges의 길이 = values의 길이 - 1
# edges의 각 행은 [v1, v2] 2개의 정수로 이루어져 있으며, 이는 v1번 노드와 v2번 노드가 연결되어 있음을 의미합니다.
# 주어진 그래프는 항상 1번 노드가 루트인 트리 형태입니다.
# 1 ≤ queries의 길이 ≤ 100,000
# queries의 각 행은 단일 쿼리를 의미하며, [u, w] 2개의 정수로 이루어져 있습니다.
# 1 ≤ u ≤ values의 길이
# -1 ≤ w ≤ 109
# w가 -1일 경우, 이 쿼리는 1번 쿼리이며, 그렇지 않을 경우 이 쿼리는 2번 쿼리입니다.
# 입출력 예
# values	edges	queries	result
# [1,10,100,1000,10000]	[[1,2],[1,3],[2,4],[2,5]]	[[1,-1],[2,-1],[3,-1],[4,-1],[5,-1],[4,1000],[1,-1],[2,-1],[3,-1],[4,-1],[5,-1],[2,1],[1,-1],[2,-1],[3,-1],[4,-1],[5,-1]]	[11111,11010,100,1000,10000,11111,10011,100,10,10000,11111,11010,100,10,10000]
# 입출력 예 설명
# 입출력 예 #1
#
# 주어진 예시는 1번 쿼리 15개와 2번 쿼리 2개로 이루어져 있습니다.
# 다음 그림은 두 2번 쿼리에 의해 트리의 노드 값들이 바뀌는 과정을 나타낸 것입니다.
# gravity_on_tree_example.png