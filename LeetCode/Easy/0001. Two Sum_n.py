class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        O(n) sol - hashmap
        note that we do this in one step so that we don't need to worry about duplicates
        """
        
        # value : index
        hmap = {}

        for i, num in enumerate(nums):
            if (target - num) in hmap:
                return [i, hmap[target-num]]
            hmap[num] = i
        


        
