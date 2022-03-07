import sys

def solution():
  # input
  input = sys.stdin.readline
  n, m = map(int, input().split())
  lengths = [0]
  for _ in range(n):
    lengths.append(int(input()))
  # DP
  DP = [0] * (n+2)
  # 뒤에서 두번째부터 시작
  for target in range(n-1, 0, -1):
    # 이 라인만 출력하고 개행했을때부터 시작
    length_sum = lengths[target]
    cost = (m - length_sum) ** 2 + DP[target+1]
    # 다음 단어도 같은 줄에 출력해보기
    ntarget = target + 1
    while ntarget <= n:
      length_sum += (lengths[ntarget] + 1)
      if length_sum > m:
        # 같은 줄에 출력했더니 너무 길때는 그만하기
        break
      # 이 단어까지만 같은 줄에 출력하고 개행했을때의 cost 계산
      ncost = ((m - length_sum) ** 2) + DP[ntarget+1]
      # 마지막 단어를 건드리고 있는경우 무조건 cost는 0
      if ntarget == n:
        ncost = 0
      cost = min(cost, ncost)
      ntarget += 1
    DP[target] = cost
  print(DP[1])

solution()