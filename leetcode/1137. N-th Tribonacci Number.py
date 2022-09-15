class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        if n < 3:
            return dp[n]
        for _ in range(n-2):
            dp.append(dp[-3] + dp[-2] + dp[-1])
        return dp[-1]