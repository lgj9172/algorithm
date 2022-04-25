class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # length = len(nums)
        # for idx1 in range(length-1):
        #     for idx2 in range(idx1+1, length):
        #         if nums[idx1] + nums[idx2] == target:
        #             return [idx1, idx2]
        pool = dict()
        for index, num in enumerate(nums):
            if (target - num) in pool:
                return [pool[target-num], index]
            pool[num] = index