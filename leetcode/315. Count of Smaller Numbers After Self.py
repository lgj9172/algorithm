class Solution:
	def countSmaller(self, nums: List[int]) -> List[int]:
		sorted_nums = sorted(nums) 
		answer = []
		for index, num in enumerate(nums):
			order = bisect_left(sorted_nums, num)
			answer.append(order)
			del(sorted_nums[order])
		return answer