class Solution:
    def threeSum(self, nums):
        nums.sort()
        answer = set()
        for indexA in range(len(nums)-2):
            A = nums[indexA]
            indexB = indexA + 1
            indexC = len(nums)-1
            while indexB < indexC:
                B = nums[indexB]
                C = nums[indexC]
                result = A + B + C
                if  result > 0:
                    indexC -= 1
                elif result < 0:
                    indexB += 1
                else:
                    indexB += 1
                    answer.add(f'{A},{B},{C}')
        return [string.split(",") for string in answer]
      
print(Solution().threeSum([-1,0,1,2,-1,-4]))