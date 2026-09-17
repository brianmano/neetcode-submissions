class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = defaultdict(list)
        squares = defaultdict(list)
        
        for i in range(9):
            rows = defaultdict(int)
            for j in range(9):

                if board[i][j] != ".":
                    if rows[board[i][j]] > 0:
                        return False
                    rows[board[i][j]] += 1

                    if board[i][j] in columns[j]:
                        return False
                    columns[j].append(board[i][j])

                    square_index = (i // 3, j // 3)  # Determine which 3x3 box this cell belongs to
                    if board[i][j] in squares[square_index]:
                        return False
                    squares[square_index].append(board[i][j])

        return True