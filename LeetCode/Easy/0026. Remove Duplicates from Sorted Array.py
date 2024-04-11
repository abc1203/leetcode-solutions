class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        approach O(N):
         - 2 ptrs
        """

        i, j = 1, 1
        while j < len(nums):
            if nums[j] != nums[j-1]:
                nums[i] = nums[j]
                i += 1
            j += 1
        
        return i
        
