# Largest Number

class Solution:
	def largestNumber(self, nums: List[int]) -> str:
		if len(nums) == 0:
			return ''

		for x in range(0, len(nums)-1):
			for y in range(x+1, len(nums)):
				a, b = str(nums[x]), str(nums[y])
				if int(a + b) < int(b + a):
					temp = nums[x]
					nums[x] = nums[y]
					nums[y] = temp

		if nums[0] == 0:
			return '0'

		result = ''
		count = 0
		while count < len(nums):
			result += str(nums[count])
			count += 1

		return result