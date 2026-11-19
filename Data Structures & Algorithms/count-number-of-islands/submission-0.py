class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = set()
        islands = 0

        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1

                    queue = deque([(r, c)])
                    visited.add((r,c))

                    while queue:
                        row, col = queue.popleft()

                        directions = [
                            (0, 1),
                            (0, -1),
                            (1, 0),
                            (-1, 0)
                        ]

                        for dr, dc in directions:
                            nr = row + dr
                            nc = col + dc

                            if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr, nc) not in visited):
                                visited.add((nr, nc))
                                queue.append((nr, nc))
        return islands



        
        

        