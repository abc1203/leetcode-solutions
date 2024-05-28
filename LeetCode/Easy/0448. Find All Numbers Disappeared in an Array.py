class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        ans = set([i for i in range(1, len(nums)+1)])
        for n in nums:
            if n in ans: ans.remove(n)
        return ans
        
