class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pool = dict()
        for index, num in enumerate(nums):
            if (target - num) in pool:
                return [pool[target-num], index]
            pool[num] = index