class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        prefix_sum = set([0])
        curr_sum = 0
        for i in range(n):
            if nums[i]%k == 0:
                if i+1 < n and nums[i+1]%k == 0: return True
            else:
                curr_sum += nums[i]
                curr_sum %= k
                if curr_sum in prefix_sum: return True
                prefix_sum.add(curr_sum)
        return False
        
