class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

         - bucket sort: O(n + Range)
         - good for smaller ranges & bad for larger ranges
        """

        hm = {}
        for n in nums:
            if n in hm: hm[n] += 1
            else: hm[n] = 1
        
        ans = []
        for n in range(min(nums), max(nums)+1):
            if n in hm: ans.extend([n]*hm[n])
        return ans

        


        
