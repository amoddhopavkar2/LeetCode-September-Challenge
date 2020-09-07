# Word Pattern

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split()
        if len(pattern) != len(words):
            return False

        dictionary = {}
        for word in words:
            if not pattern[0] in dictionary.values() and not word in dictionary:
                dictionary[word] = pattern[0]
            else:
                if not word in dictionary or dictionary[word] != pattern[0]:
                    return False
            pattern = pattern[1:]
        return True