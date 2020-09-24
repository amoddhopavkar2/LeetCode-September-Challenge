# Find the Difference

from collections import Counter
class Solution:
	def findTheDifference(self, s: str, t: str) -> str:
		counter_s = Counter(s)
		counter_t = Counter(t)

		for x in counter_t:
			if x not in counter_s or counter_t[x] != counter_s[x]:
				return str(x)