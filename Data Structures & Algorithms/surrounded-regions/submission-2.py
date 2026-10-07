class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        marked = set()
        directions =[
            (0, 1),
            (0, -1),
            (1, 0),
            (-1,0)
        ]
        
        for i in range(ROWS):
            if board[i][0] == "O":
                marked.add((i, 0))
            if board[i][COLS-1] == "O":
                marked.add((i, COLS-1))
        for i in range(COLS):
            if board[ROWS-1][i] == "O":
                marked.add((ROWS - 1, i))
            if board[0][i] == "O":
                marked.add((0, i))
        
        def bfs(options):
            q = deque(options)
            while q:
                r, c = q.popleft()
            
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in marked and board[nr][nc] == "O"):
                        q.append((nr, nc))
                        marked.add((nr, nc))
        bfs(marked)
        print(marked)
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in marked:
                    board[i][j] = "X"
        
