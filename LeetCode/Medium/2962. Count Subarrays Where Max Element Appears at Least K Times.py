class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

         - sliding window
        """

        maxNums = max(nums)
        count = 0
        ans = 0

        l = 0
        for r in range(len(nums)):
            if nums[r] == maxNums: count += 1

            while count >= k:
                if nums[l] == maxNums: count -= 1
                l += 1
            ans += l
        return ans



        
        
        
