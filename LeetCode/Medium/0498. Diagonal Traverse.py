class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        m,n = len(mat), len(mat[0])
        x,y = 0,0
        dir = [(0, 1), (1, 0)]
        ans = [mat[x][y]]

        while (x, y) != (m-1, n-1):
            for dx,dy in dir:
                x += dx
                y += dy
                if 0 <= x < m and 0 <= y < n: ans.append(mat[x][y])

                if (dx,dy) == (0,1):
                    while 0 <= x+1 < m and 0 <= y-1 < n:
                        x += 1
                        y -= 1
                        ans.append(mat[x][y])
                elif (dx,dy) == (1,0):
                    while 0 <= x-1 < m and 0 <= y+1 < n:
                        x -= 1
                        y += 1
                        ans.append(mat[x][y])
                if (x, y) == (m-1, n-1): break

        return ans
            



        
