from collections import deque

N, K = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([False] * N)
round = 0
while True:
    # 벨트 회전
    round += 1
    robot[-1] = False
    belt.rotate(1)
    robot.rotate(1)
    # 뒤쪽부터 한칸씩 이동
    for index in range(N - 1, -1, -1):
        if index == N - 1:
            robot[index] = False
        else:
            if (
                robot[index] == True
                and robot[index + 1] == False
                and belt[index + 1] > 0
            ):
                robot[index + 1] = True
                belt[index + 1] -= 1
                robot[index] = False
    # 로봇 올리기
    if robot[0] == False and belt[0] > 0:
        robot[0] = True
        belt[0] -= 1
    # 조건확인
    if belt.count(0) >= K:
        break
print(round)