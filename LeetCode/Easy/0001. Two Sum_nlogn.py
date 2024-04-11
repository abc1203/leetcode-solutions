class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        O(nlogn) sol - sort & 2 ptrs
        """
        
        nums_copy = nums[:]
        nums_copy.sort()
        left, right = 0, len(nums) - 1
        
        while left <= right:
            if nums_copy[left] + nums_copy[right] == target: break
            elif nums_copy[left] + nums_copy[right] < target: left += 1
            elif nums_copy[left] + nums_copy[right] > target: right -= 1
        
        ans = []
        for i in range(len(nums)):
            if nums[i] == nums_copy[left] or nums[i] == nums_copy[right]: ans.append(i)
        return ans

        
