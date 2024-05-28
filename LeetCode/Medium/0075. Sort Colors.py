class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        approach 1 (O(N) 2-pass with O(1) extra space): bucket sort
        approach 2 (O(N) 1-pass with O(1) extra space): dutch national flag
             - maintains 3 ptrs low, mid, high s.t. all 0s before low, all 2s after high
             - moves mid; 
                1. if encounters 0, swap with low and increment both
                2. if encounters 2, swap with high and decrement high
                3. if encounters 1, increment mid
        """

        # approach 1
        # hm = {}
        # for n in nums:
        #     if n not in hm: hm[n] = 1
        #     else: hm[n] += 1
        
        # j = 0
        # for i in range(3):
        #     if i in hm:
        #         while hm[i] > 0:
        #             nums[j] = i
        #             hm[i] -= 1
        #             j += 1

        low, mid, high = 0, 0, len(nums)-1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        

        
