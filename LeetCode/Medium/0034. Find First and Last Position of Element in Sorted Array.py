class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binSearch(tar):
            l, r = 0, len(nums)-1
            while l <= r:
                m = (l+r)/2
                if nums[m] == tar: return m
                elif nums[m] < tar: l = m + 1
                else: r = m - 1
            return l
        
        idx = binSearch(target)
        if idx < 0 or idx >= len(nums) or nums[binSearch(target)] != target: return [-1, -1]
        return [binSearch(target-0.5), binSearch(target+0.5)-1]
        
        
