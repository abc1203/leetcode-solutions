class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """

        def checkDiag(x, y):
            val = matrix[x][y]

            while 0 <= x+1 < m and 0 <= y+1 < n:
                x += 1
                y += 1
                if matrix[x][y] != val: 
                    return False
            return True
            
        m,n = len(matrix), len(matrix[0])

        for i in range(n-1, -1, -1):
            x,y = 0,i
            if not checkDiag(x, y): return False
        
        for i in range(1, m):
            x,y = i,0
            if not checkDiag(x, y): return False
   
        return True



        
