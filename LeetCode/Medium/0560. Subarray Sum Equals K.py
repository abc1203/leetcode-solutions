class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        idea O(N) (prefix sum):
         - for each iter i, we add prefixSum[i] to hashmap
         - when we find that a sum-k exists in hm, that means:
            current index i = sum
            exists an index j with prefixSum = sum - k
            then j to i is a solution
         - note that it's possible to have multiple j (thus hashmap stores the count)
        """

        hm = {}
        hm[0] = 1
        ans, sum = 0, 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum-k in hm:
                ans += hm[sum-k]
            hm[sum] = 1 + hm.get(sum, 0)
        return ans


        # O(N^2) approach
        # ans = 0
        # for i in range(len(nums)):
        #     j = i
        #     sumRow = 0

        #     while j < len(nums):
        #         sumRow += nums[j]
        #         if sumRow == k: ans += 1
        #         j += 1
        # return ans
        
