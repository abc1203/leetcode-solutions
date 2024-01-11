class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        Algo:
        1. calculate product for a[0], a[0] * a[1], a[0] * a[1] * a[2], ...
        2. calculate product for a[n-1], a[n-1] * a[n-2], ...
        3. res[i] = forward[i-1] * backward[n-i+1]
        """
        forward = [1] * len(nums)
        backward = [1] * len(nums)
        res = [1] * len(nums)

        forward_product = 1
        backward_product = 1
        for i in range(0, len(nums)):
            forward_product *= nums[i]
            forward[i] = forward_product
            backward_product *= nums[len(nums)-i-1]
            backward[i] = backward_product
        
        for i in range(0, len(nums)):
            if i == 0: res[i] = backward[(len(nums)-1)-(i+1)]
            elif i == len(nums)-1: res[i] = forward[i-1]
            else: res[i] = forward[i-1] * backward[(len(nums)-1)-(i+1)]

        return res
      
