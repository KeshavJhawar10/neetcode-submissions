from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        q = deque()
        fresh_oranges = 0
        for i in range (len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1
        directions = [
            [1, 0],
            [-1, 0],
            [0, -1],
            [0, 1]
        ]
        while q and fresh_oranges > 0:
            for _ in range(len(q)):
                i, j = q.popleft()
                
                for dirs in directions:
                    di, dj = dirs
                    ni, nj = i + di, j + dj
                    if (0 <= ni < len(grid) and 0 <= nj < len(grid[0])):
                        if grid[ni][nj] == 1:
                            grid[ni][nj] = 2
                            q.append((ni, nj))
                            fresh_oranges -=1

            minutes +=1
        return -1 if fresh_oranges > 0 else minutes
                
            
