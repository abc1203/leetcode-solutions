class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool

        idea:
         - check if board[row][col] == word[i]
         - if equals and is not in previous path, check the surroundings
         - remove (row, col) from prev_paths s.t. it can be used for other paths
        """

        prev_coords = set()

        def iterate(row, col, i):
            if i >= len(word): return True
            elif (row < 0 or row >= len(board)) or \
                (col < 0 or col >= len(board[row])): return False
            elif board[row][col] != word[i]: return False
            elif (row, col) in prev_coords: return False

            prev_coords.add((row, col))

            exists = (iterate(row+1, col, i+1) or \
                    iterate(row-1, col, i+1) or \
                    iterate(row, col+1, i+1) or \
                    iterate(row, col-1, i+1))
            
            prev_coords.remove((row, col))
            return exists
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    exists = iterate(i, j, 0)
                    if exists: return True
        
        return False

