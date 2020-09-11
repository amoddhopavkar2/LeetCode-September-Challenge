# Maximum Product Subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
    	current_max = current_min = previous_max = previous_min = nums[0]
    	result = nums[0]

    	for i in range(1, len(nums), 1):
    		current_max = max(previous_max * nums[i], previous_min * nums[i], nums[i])
    		current_min = min(previous_max * nums[i], previous_min * nums[i], nums[i])
    		result = max(current_max, result)
    		previous_max = current_max
    		previous_min = current_min

    	return result
    	