# Maximum XOR of Two Numbers in an Array

class Solution:
	def findMaximumXOR(self, nums: List[int]) -> int:
		result = 0

		for i in reversed(range(32)):
			result <<= 1
			prefixes = set()

			for n in nums:
				prefixes.add(n >> i)
			for p in prefixes:
				if (result | 1) ^ p in prefixes:
					result += 1
					break

		return result