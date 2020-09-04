# Partition Labels

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        result = []
        last_indices = [0] * 26

        for i in range(len(S)):
            last_indices[ord(S[i]) - ord('a')] = i

        start = end = 0
        for i in range(len(S)):
            end = max(end, last_indices[ord(S[i]) - ord('a')])
            if end == i:
                result.append(end - start + 1)
                start = end + 1

        return result
