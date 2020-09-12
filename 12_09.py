# Combination Sum III

class Solution(object):
    def _combinationSum3Helper(self, remaining, candidates, next_value, partial_sum, target):
        result = []
        if remaining == 0:
            if partial_sum == target:
                combination = []
                for i in range(1, next_value):
                    if candidates[i] == True:
                        combination.append(i)
                result.append(combination)
                return result
            else:
                return result
        elif partial_sum + next_value > target or next_value > 9:
            return result
        else:
            result.extend(self._combinationSum3Helper(
                remaining, candidates, next_value + 1, partial_sum, target))
            candidates[next_value] = True
            result.extend(self._combinationSum3Helper(
                remaining - 1, candidates, next_value + 1, partial_sum + next_value, target))
            candidates[next_value] = False
            return result

    def combinationSum3(self, k, n):
        candidates = [False for _ in range(10)]
        return self._combinationSum3Helper(k, candidates, 1, 0, n)
