from collections import deque
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates_count = len(candidates)
        answer = []
        queue = deque()
        for i, e in enumerate(candidates):
          queue.append([e, i, [e]]) # sum, index, history
        while queue:
          s, i, history = queue.popleft()
          if s > target:
            continue
          if s == target:
            answer.append(history)
            continue
          for ni in range(i, candidates_count):
            candidate = candidates[ni]
            queue.append([s+candidate, ni, history+[candidate]])
        return answer