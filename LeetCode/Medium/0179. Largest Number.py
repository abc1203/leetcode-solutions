class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if set(nums) == set([0]): return '0'
        return ''.join(sorted([str(num) for num in nums], key=lambda x: x*10, reverse=True))

        
        
