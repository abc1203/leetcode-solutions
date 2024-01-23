class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        idea: 
        use binary search with l = 0 & r = len(nums)-1
        calculate mid & compare value(mid) with r
        """

        l, r = 0, len(nums)-1
        ans = nums[l]
        while l <= r:
            mid = (l + r) / 2
            ans = min(ans, nums[mid])

            if nums[mid] < nums[r]:
                r = mid - 1
            else: 
                l = mid + 1
        
        return ans
        
