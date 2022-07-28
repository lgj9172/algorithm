class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        answer = 0
        for a, b in zip(heights, sorted(heights)):
            if a != b:
                answer += 1
        return answer