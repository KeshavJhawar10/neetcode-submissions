from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.max_area = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        def bfs(r, c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            curr_area = 1
            directions = [[-1, 0], [1,0], [0, -1], [0, 1]]
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = dr + row, dc + col
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1 and (r,c) not in visited:
                        visited.add((r,c))
                        q.append((r,c))
                        curr_area +=1
                    self.max_area = max(self.max_area, curr_area)
        
        for i in range(rows):
            for j in range(cols):
                if (grid[i][j] == 1 and (i,j) not in visited):
                    bfs(i, j)
        return self.max_area