# Round Bounded in Circle

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        i, j, di, dj = 0, 0, 0, 1

        for move in instructions:
            if move == 'G':
                i, j = i+di, j+dj
            elif move == 'L':
                di, dj = -dj, di
            else:
                di, dj = dj, -di

        return i == j == 0 or (di, dj) != (0, 1)