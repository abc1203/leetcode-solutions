class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        approach O(N):
        1. find a breakpoint i from the back where nums[i] < nums[i+1]
        2. find the smallest elem > nums[i] in the right side & swap them
        3. reverse the right side
        """

        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                minVal, minInd = nums[i+1], i+1
                for j in range(i+1, len(nums)):
                    if nums[j] <= minVal and nums[j] > nums[i]:
                        minVal, minInd = nums[j], j
                
                nums[i], nums[minInd] = nums[minInd], nums[i]

                nums[i+1:] = nums[i+1:][::-1]
                return nums
        
        return nums.reverse()
