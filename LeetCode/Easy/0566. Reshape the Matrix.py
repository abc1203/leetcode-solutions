class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        old_r, old_c = len(mat), len(mat[0])
        if old_r * old_c != r * c: return mat

        ans = [[-1]*c for _ in range(r)]

        new_i, new_j = 0,0
        for i in range(old_r):
            for j in range(old_c):
                ans[new_i][new_j] = mat[i][j]
                new_j += 1

                if new_j == c:
                    new_i += 1
                    new_j = 0
        return ans

        
