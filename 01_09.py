# Largest Time for Given Digits

from itertools import permutations
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
    	A.sort(reverse = True)
    	arr = list(permutations(A))

    	for h1, h2, m1, m2 in arr:
    		hrs = h1 * 10 + h2
    		mins = m1 * 10 + m2

    		if hrs < 24 and mins < 60:
    			return "{}{}:{}{}".format(h1, h2, m1, m2)
    	return ""