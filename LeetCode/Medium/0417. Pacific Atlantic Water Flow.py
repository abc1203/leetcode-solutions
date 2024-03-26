class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]

        idea:
         - have 2 sets: one is the pos that can flow to pacific & one is atlantic
         - run dfs on each edge pos; only continue iterating if the new height is bigger
         - this means that the new pos have hgiher heights => can flow
        """
        ans = []
        pac, atl = set(), set()

        def dfs(row, col, visited, prev):
            if (
                (row, col) in visited or \
                row < 0 or col < 0 or row == len(heights) or col == len(heights[0]) or \
                heights[row][col] < prev
            ):
                return
            
            visited.add((row, col))

            # check neighboring pos
            dfs(row+1, col, visited, heights[row][col])
            dfs(row-1, col, visited, heights[row][col])
            dfs(row, col+1, visited, heights[row][col])
            dfs(row, col-1, visited, heights[row][col])
        
        # run dfs on each edge pos
        for r in range(len(heights)):
            dfs(r, 0, pac, 0)
            dfs(r, len(heights[0])-1, atl, 0)
        for c in range(len(heights[0])):
            dfs(0, c, pac, 0)
            dfs(len(heights)-1, c, atl, 0)
        
        for (r, c) in pac:
            if (r, c) in atl: ans.append([r, c])
        
        return ans


        
