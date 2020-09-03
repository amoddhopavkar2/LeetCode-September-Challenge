# Repeated Substring Pattern

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        string_len = len(s)
        for i in range(string_len // 2, 0, -1):
            if string_len % i == 0:
                repeats = string_len // i
                new_string = ""
                sub_string = s[:i]
                for j in range(repeats):
                    new_string += sub_string

                if new_string == s:
                    return True

            return False
