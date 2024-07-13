class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) <= 2: return True

        order = set()

        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] > 0: order.add(1)
            elif nums[i+1] - nums[i] == 0: order.add(0)
            elif nums[i+1] - nums[i] < 0: order.add(-1)
            
            if 1 in order and -1 in order: return False
        
        return True

        
