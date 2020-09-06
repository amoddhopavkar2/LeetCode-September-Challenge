# Image Overlap

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        N = len(A)
        best = 0

        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            for shiftx in range(N):
                for shifty in range(N):
                    count = 0

                    for x in range(N):
                        for y in range(N):
                            if A[x][y] == 1:
                                nx = x + shiftx * dx
                                ny = y + shifty * dy

                                if 0 <= nx < N and 0 <= ny < N and B[nx][ny] == 1:
                                    count += 1
                    best = max(best, count)
        return best
