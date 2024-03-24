class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int

        idea:
         - run dfs
        """
        ans = 0
        visited = set()
        r_len, c_len = len(grid), len(grid[0])

        def dfs(row, col):
            if (row, col) in visited or \
                row not in range(r_len) or \
                col not in range(c_len) or \
                grid[row][col] == "0":
                return
            
            visited.add((row, col))

            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
        
        for i in range(r_len):
            for j in range(c_len):
                if grid[i][j] == "1" and (i, j) not in visited:
                    ans += 1
                    dfs(i, j)

        return ans

        
