# Teemo Attacking

class Solution:
	def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
		if len(timeSeries) == 0:
			return 0

		result = 0
		for i in range(1, len(timeSeries)):
			result += min(timeSeries[i] - timeSeries[i-1], duration)

		return result + duration

