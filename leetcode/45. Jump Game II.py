from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
      jump_count, zone_start, zone_end = 0, 0, 0
      while zone_end < len(nums)-1:
        jump_count += 1
        max_jump = max([index+jump for index, jump in enumerate(nums[zone_start:zone_end+1])])
        zone_start, zone_end = zone_end + 1, zone_start + max_jump
      return jump_count
        
      

# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         length = len(nums)
#         answer = [length]*length
#         answer[0] = 0
#         for index, num in enumerate(nums):
#             hop = answer[index]
#             for target_index in range(index+1, index+num+1):
#                 if target_index < length:
#                     if answer[target_index] > hop+1:
#                         answer[target_index] = hop+1
#         return answer[len(nums)-1]
      
print(Solution().jump([2,3,1,1,4]))
# print(Solution().jump([0]))
# print(Solution().jump([3,4,3,2,5,4,3]))
