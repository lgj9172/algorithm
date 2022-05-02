class Solution:
    def numSquares(self, n: int) -> int:
        squares = [e**2 for e in range(1, int(n ** 0.5)+1)]
        dp = [1] * (n+1)
        for i in range(2, n+1):
          value = i
          for square in squares:
            if i-square>=1 and dp[i-square]<value:
              value = dp[i-square]+1
            elif i-square==0:
              value = 1
          dp[i] = value
        return dp[n]

print(Solution().numSquares(12))