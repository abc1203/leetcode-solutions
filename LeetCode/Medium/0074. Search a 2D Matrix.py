class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool

        idea:
        apply binary search on the rows first using min & max values
        as such we find a row s.t. min_row <= target <= max_row (O(logm))
        Then apply binary search on the row O(logn)
        """

        def binarySearch(row, target):
            l, r = 0, len(row)-1
            while l <= r:
                mid = (l + r) / 2
                if row[mid] == target: return True
                elif row[mid] < target: l = mid + 1
                else: r = mid - 1
            return False

        l_row, r_row = 0, len(matrix)-1
        while l_row <= r_row:
            curr_row = (l_row + r_row) / 2
            if matrix[curr_row][0] <= target and target <= matrix[curr_row][len(matrix[curr_row])-1]:
                return binarySearch(matrix[curr_row], target)
            elif target < matrix[curr_row][0]:
                r_row = curr_row - 1
            elif target > matrix[curr_row][len(matrix[curr_row])-1]:
                l_row = curr_row + 1
        
        return False
        
