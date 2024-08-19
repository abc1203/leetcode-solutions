class Solution(object):
    def validSubarraySize(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        
        idea (stack):
         - create an increasing stack (index)
         - whenever an element is popped, check if that element forms a good subarray
         - from stack[-1] to the current element
         - works bc the current element is a local min, so check the indices before it
        """
        nums = [0] + nums + [0]
        stack = [0]

        for i in range(1, len(nums)):
            while nums[i] < nums[stack[-1]]:
                top = nums[stack.pop()]

                if top > threshold / (i - stack[-1] - 1):
                    return i - stack[-1] - 1
            stack.append(i)
        return -1


        
