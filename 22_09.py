# Majority Element II

from collections import Counter
class Solution:
	def majorityElement(self, nums: List[int]) -> List[int]:
		result = []
		key = len(nums) // 3

		lst = Counter(nums)
		for x in lst:
			if lst[x] > key:
				result.append(x)

		return result