class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j))
        
        directions = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]
        while q:
            i, j = q.popleft()

            for di, dj in directions:
                ni = i + di
                nj = j + dj

                if ( 
                    0 <= ni < rows and 0 <= nj < cols and grid[ni][nj]== 2147483647
                ):
                    grid[ni][nj] = grid[i][j] + 1
                    q.append((ni, nj))