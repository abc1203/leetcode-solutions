class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        matrix = [[0]*n for _ in range(n)]
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x,y = 0,0
        curr, final = 1, n**2
        matrix[x][y] = curr

        while True:
            for dx, dy in dir:
                while 0 <= x+dx < n and 0 <= y+dy < n and matrix[x+dx][y+dy] == 0:
                    x += dx
                    y += dy
                    curr += 1
                    matrix[x][y] = curr
            
            if curr == final: break
        
        return matrix
                

        
