class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        for _ in range(n-2):
            dp.append(dp[-3] + dp[-2] + dp[-1])
        return dp[-1]