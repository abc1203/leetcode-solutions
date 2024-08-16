class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        visited = set()
        m, n = len(matrix), len(matrix[0])
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0
        ans = [matrix[x][y]]
        visited.add((0, 0))

        while len(visited) < m*n:
            for dx, dy in dir:
                while 0 <= x+dx < m and 0 <= y+dy < n and (x+dx, y+dy) not in visited:
                    x += dx
                    y += dy
                    ans.append(matrix[x][y])
                    visited.add((x, y))
        
        return ans




        
