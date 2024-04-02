class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.

        idea:
         - note that for 'O' to be NOT captured, it must be connected to an edge
         - so mark the ones that are on the edge, then capture the unmarked ones
        """

        def dfs(r, c):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or \
                board[r][c] != 'O': return

            board[r][c] = 'M'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        # mark 
        for r in range(len(board)):
            dfs(r, 0)
            dfs(r, len(board[0])-1)
        for c in range(len(board[0])):
            dfs(0, c)
            dfs(len(board)-1, c)
        
        # capture
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O': board[r][c] = 'X'

        # unmark
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'M': board[r][c] = 'O'
