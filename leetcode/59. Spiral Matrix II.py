from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        answer = [[0] * n for _ in range(n)]
        row, col, count, round = 0, 0, 1, 0
        while round < n//2:
          for i in range(n-round*2-1):
            answer[row][col] = count
            col += 1
            count += 1
          for i in range(n-round*2-1):
            answer[row][col] = count
            row += 1
            count += 1
          for i in range(n-round*2-1):
            answer[row][col] = count
            col -= 1
            count += 1
          for i in range(n-round*2-1):
            answer[row][col] = count
            row -= 1
            count += 1
          row, col = row+1, col+1
          round += 1
        if n%2==1:
          answer[n//2][n//2] = count
        return answer

Solution().generateMatrix(4)