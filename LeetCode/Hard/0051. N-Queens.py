class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]

        idea:
         - since we're placing n queens in nxn, each row must have exactly 1 queen
         - so we start from row 0 and fill row by row
         - also note that the diagonals can be found using (r+c) and (r-c)
        """

        occupied_col = set()
        pos_diag = set() 
        neg_diag = set()

        ans = set()
        curr_board = [["."] * n for i in range(n)]

        def iterate(row):
            if row == n: 
                board_tup = tuple(["".join(row) for row in curr_board])
                if board_tup not in ans: ans.add(board_tup)
                return

            for col in range(n):
                # if queen can't be placed in (row, col), continue
                if col in occupied_col or (row+col) in pos_diag or (row-col) in neg_diag: 
                    continue

                curr_board[row][col] = "Q"
                occupied_col.add(col)
                pos_diag.add(row+col)
                neg_diag.add(row-col)

                iterate(row+1)
                
                curr_board[row][col] = "."
                occupied_col.remove(col)
                pos_diag.remove(row+col)
                neg_diag.remove(row-col)
        
        iterate(0)
        return ans



        
