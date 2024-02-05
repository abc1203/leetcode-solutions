class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        idea (dp):
        on the ith iteration:
        cur_max = max subarray product from 0 to i with last elem being i
        cur_min = min subarray product from 0 to i with last elem being i
        """

        cur_max, cur_min = nums[0], nums[0]
        ans = cur_max
        for i in range(1, len(nums)):
            cur_max, cur_min = max(cur_max * nums[i], nums[i], cur_min * nums[i]),\
                            min(cur_max * nums[i], nums[i], cur_min * nums[i])

            ans = max(ans, cur_max)
        
        return ans


        
