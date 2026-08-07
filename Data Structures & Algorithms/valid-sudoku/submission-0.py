class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in col[j] or
                    board[i][j] in rows[i] or 
                    board[i][j] in squares[(i // 3, j //3)]):
                    return False
                rows[i].add(board[i][j])
                col[j].add(board[i][j])
                row = i // 3
                column = i // 3
                squares[(i//3, j//3)].add(board[i][j])


        return True