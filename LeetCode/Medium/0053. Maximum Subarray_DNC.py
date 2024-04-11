class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        approach #1 (DNC - O(nlogn)):
         - find max subarray with left & right
         - then compare with the max subarray that contains mid - take the larger one
         - doesn't work if the values are NOT unique
        """

        if len(nums) == 1: return nums[0]
        
        m = len(nums) / 2
        left, right = nums[:m], nums[m:]
        lSum, rSum = self.maxSubArray(left), self.maxSubArray(right)

        mSum = 0
        if len(nums) % 2 == 0:
            l, r = m-1, m
            mSum = nums[l] + nums[r]
            l -= 1
            r += 1
        else:
            mSum = nums[m]
            l, r = m-1, m+1

        maxSum = mSum
        while l >= 0 or r < len(nums):    
            if l >= 0 and r < len(nums):
                if nums[l] > nums[r]:
                    mSum += nums[l]
                    l -= 1
                else:
                    mSum += nums[r]
                    r += 1
            elif l >= 0:
                mSum += nums[l]
                l -= 1
            elif r < len(nums):
                mSum += nums[r]
                r += 1
            maxSum = max(maxSum, mSum)
        
        return max(maxSum, max(lSum, rSum))

                    

        
