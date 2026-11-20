from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxA = 0
        queue = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 1:
                    queue.append((r, c))
                    curA = 1
                    grid[r][c] = 0
                    while queue:
                        cr, cc = queue.popleft()
                        for dr, dc in directions:
                            nr, nc = cr + dr, cc + dc
                            if (0 <= nr < len(grid) and 0 <= nc < len(row) 
                                and grid[nr][nc] == 1):

                                queue.append((nr, nc))
                                curA += 1
                                grid[nr][nc] = 0

                    maxA = max(maxA, curA)


        return maxA