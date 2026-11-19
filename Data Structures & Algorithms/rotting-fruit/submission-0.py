from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        time = 0
        freshC = 0
        queue = deque()

        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    queue.append((r, c))
                elif val == 1:
                    freshC += 1
        
        while freshC > 0 and queue:
            count = len(queue)
            for _ in range(count):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < len(grid) and 0 <= nc < len(grid[0]) 
                        and grid[nr][nc] == 1):
                        freshC -= 1
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
            time += 1


        if freshC != 0:
            return -1
        return time
        