class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1] * 45
        for i in range(2, n+1):
          dp[i] = dp[i-1] + dp[i-2]
        print(dp[n])
        
print(Solution().climbStairs(2))