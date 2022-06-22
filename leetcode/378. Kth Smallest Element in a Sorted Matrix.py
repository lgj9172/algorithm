class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return sorted(reduce(lambda acc,cur:acc+cur, matrix, []))[k-1]