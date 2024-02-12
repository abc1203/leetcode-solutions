class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int

        dp[i][j] = length of longest incr path starting from (i, j)
        """

        dp = [[0] * len(matrix[0]) for i in range(len(matrix))]

        def backtrack(row, col):
            if row < 0 or row >= len(matrix): return 0
            elif col < 0 or col >= len(matrix[row]): return 0
            elif dp[row][col] != 0: return dp[row][col]

            longest = 1
            curr_val = matrix[row][col]
            if row-1 >= 0 and matrix[row-1][col] > curr_val:
                longest = max(longest, 1 + backtrack(row-1, col))
            if row+1 < len(matrix) and matrix[row+1][col] > curr_val:
                longest = max(longest, 1 + backtrack(row+1, col))
            if col-1 >= 0 and matrix[row][col-1] > curr_val:
                longest = max(longest, 1 + backtrack(row, col-1))
            if col+1 < len(matrix[row]) and matrix[row][col+1] > curr_val:
                longest = max(longest, 1 + backtrack(row, col+1))

            dp[row][col] = longest
            return longest
        
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                ans = max(ans, backtrack(i, j))
        return ans

        
