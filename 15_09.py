# Length of Last Word

class Solution:
	def lengthOfLastWord(self, s: str) -> int:
		strings = s.split()

		if len(strings) == 0:
			return 0
		return len(strings[-1])