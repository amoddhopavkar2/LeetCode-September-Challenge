# House Robber
# Solve by using Dynamic Programming

class Solution:
	def rob(self, nums: List[int]) -> int:
		n = len(nums)

		if n == 0:
			return 0
		if n == 1:
			return nums[0]
		if n == 2:
			return max(nums[0], nums[1])

		max_robbery = [0] * n
		max_robbery[0] = nums[0]
		max_robbery[1] = max(nums[0], nums[1])

		for i in range(2, n):
			max_robbery[i] = max((nums[i] + max_robbery[i-2]), max_robbery[i-1])

		return max_robbery[-1]