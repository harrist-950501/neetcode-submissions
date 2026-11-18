from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        queue = deque()
        derection = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        count = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == "1":
                    count += 1
                    queue.append((r, c))
                    grid[r][c] = "0"
                    while queue:
                        (cr, cc) = queue.popleft()
                        for ar, ac in derection:
                            nr, nc = cr + ar, cc + ac
                            if 0 <= nr < len(grid) and 0 <= nc < len(row) and grid[nr][nc] == "1":
                                queue.append((nr, nc))
                                grid[nr][nc] = "0"
        
        return count