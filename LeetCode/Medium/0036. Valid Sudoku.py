BOARD_LEN = 9
SQR_LEN = 3

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool

        algo:
        for each coordinate: check if it's valid in its row, col & square
        """
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for i in range(0, BOARD_LEN):
            for j in range(0, BOARD_LEN):
                if board[i][j] != ".":
                    if (board[i][j] in rows[i]) or (board[i][j] in cols[j]) or(board[i][j] in squares[(i // SQR_LEN, j // SQR_LEN)]):
                        return False
                    else:
                        rows[i].add(board[i][j])
                        cols[j].add(board[i][j])
                        squares[(i // SQR_LEN, j // SQR_LEN)].add(board[i][j])
    
        return True

    
