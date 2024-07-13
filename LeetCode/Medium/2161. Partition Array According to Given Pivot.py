class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """

        lower, equal, greater = 0, 0, 0
        for n in nums:
            if n < pivot: lower += 1
            elif n == pivot: equal += 1
        
        # starting idx of greater
        greater = lower + equal
        equal, lower = lower, 0

        ans = [0] * len(nums)
        for n in nums:
            if n < pivot: 
                ans[lower] = n
                lower += 1
            elif n == pivot:
                ans[equal] = n
                equal += 1
            else:
                ans[greater] = n
                greater += 1
        return ans

        
