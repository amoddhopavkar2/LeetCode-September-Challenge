# Sequential Digits

import collections
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        digits = collections.deque(range(1, 9))

        while digits:
            num = digits.popleft()
            if num > high:
                continue
            if low <= num:
                result.append(num)
            if num % 10 + 1 < 10:
                digits.append(num*10 + num%10 + 1)
        return result