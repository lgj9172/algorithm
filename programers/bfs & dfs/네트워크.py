from collections import deque


def solution(n, computers):
    answer = 0
    history = set()
    for computer_number in range(n):
        if computer_number not in history:
            BFS(n, computers, computer_number, history)
            answer += 1
    return answer


def BFS(n, computers, computer_number, history):
    history.add(computer_number)
    queue = deque()
    queue.append(computer_number)
    while queue:
        target = queue.popleft()
        history.add(target)
        for next in range(n):
            if next != target and computers[target][next] == 1:
                if next not in history:
                    queue.append(next)