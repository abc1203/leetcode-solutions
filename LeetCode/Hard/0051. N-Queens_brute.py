class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        ans = set()
        curr_board = [["."] * n for i in range(n)]

        def canBePlaced(r, c):
            # check same row
            for i in range(n):
                if curr_board[r][i] == "Q": return False

                # check same col
                if curr_board[i][c] == "Q": return False
            
                # check diagonals
                if r+i>=0 and r+i<n and c+i>=0 and c+i<n and curr_board[r+i][c+i] == "Q": return False
                if r+i>=0 and r+i<n and c-i>=0 and c-i<n and curr_board[r+i][c-i] == "Q": return False
                if r-i>=0 and r-i<n and c+i>=0 and c+i<n and curr_board[r-i][c+i] == "Q": return False
                if r-i>=0 and r-i<n and c-i>=0 and c-i<n and curr_board[r-i][c-i] == "Q": return False

            return True

        def iterate(num_queens, row, col):
            if num_queens == 0: 
                board_tup = tuple(["".join(row) for row in curr_board])
                if board_tup not in ans: ans.add(board_tup)
                return
            
            # check if queen can be placed in (row, col)
            if canBePlaced(row, col):
                curr_board[row][col] = "Q"

                for i in range(n):
                    for j in range(n):
                        iterate(num_queens-1, i, j)
                
                curr_board[row][col] = "."
        
        for i in range(n):
            for j in range(n):
                iterate(n, i, j)
        
        return ans



        
