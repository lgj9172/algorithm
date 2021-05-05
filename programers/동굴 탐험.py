from collections import defaultdict, deque

def solution(n, path, order):
    pending, visited = [False] * n, [False] * n
    v = defaultdict(list)
    for start, end in path:
        v[start].append(end)
        v[end].append(start)
    get_before = {v: k for k, v in order}
    before_set = {k for k, v in order}
    get_next = {k: v for k, v in order}
    next_set = {v for k, v in order}
    queue = deque([0])
    while queue:
        target = queue.popleft()
        # 다른곳에 다녀왔는지 체크해야되는 경우
        if target in next_set:
            # 다른곳에 아직 가보지 못한 경우
            if visited[get_before[target]] is False:
                # 이 노드는 대기 표시
                pending[target] = True
                continue
        # 출발하는 곳인데
        elif target in before_set:
            # 이곳에서 출발하기를 기다리는 경우
            if pending[get_next[target]]:
                # 큐에 도착할 곳 다시 추가
                queue.append(get_next[target])
        # 아직 갔던 곳이 아니면 큐에 추가
        nexts = v[target]
        for next in nexts:
            if not visited[next]:
                queue.append(next)
        visited[target] = True
    return True if sum(visited) == n else False


if __name__ == '__main__':
    print(solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[8, 5], [6, 7], [4, 1]]))
    print(solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[4, 1], [8, 7], [6, 5]]))
