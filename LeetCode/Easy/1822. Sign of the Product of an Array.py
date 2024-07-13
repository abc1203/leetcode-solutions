class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        product = 1
        for n in nums: product *= n

        if product > 0: return 1
        elif product < 0: return -1
        return 0
        
