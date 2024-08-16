class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m,n = len(matrix), len(matrix[0])
        new_mat = [[0]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                new_mat[i][j] = matrix[j][i]
        return new_mat

        
