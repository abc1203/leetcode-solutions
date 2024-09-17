class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])

        valid_path = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

        q = [(0, 0)]
        visited = set()
        while q:
            x, y = q.pop(0)
            if x == m-1 and y == n-1: return True

            if 0<=x<m and 0<=y<n and (x, y) not in visited:
                visited.add((x, y))
                for dx, dy in valid_path[grid[x][y]]:
                    new_x, new_y = x+dx, y+dy

                    if 0<=new_x<m and 0<=new_y<n and (new_x, new_y) not in visited and \
                    (-dx, -dy) in valid_path[grid[new_x][new_y]]:
                        q.append((new_x, new_y))
        return False


        
