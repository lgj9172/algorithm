N = int(input())
max_dp = [0, 0, 0]
min_dp = [0, 0, 0]
for i in range(N):
    A, B, C = map(int, input().split())
    max_a = max(max_dp[0], max_dp[1]) + A
    max_b = max(max_dp[0], max_dp[1], max_dp[2]) + B
    max_c = max(max_dp[1], max_dp[2]) + C
    min_a = min(min_dp[0], min_dp[1]) + A
    min_b = min(min_dp[0], min_dp[1], min_dp[2]) + B
    min_c = min(min_dp[1], min_dp[2]) + C
    max_dp = [max_a, max_b, max_c]
    min_dp = [min_a, min_b, min_c]
print(max(max_dp), min(min_dp))