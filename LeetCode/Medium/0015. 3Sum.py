class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        algo: 
        1. sort nums
        2. start from 1st elem - use 2 pointers to find the rest of 2 elem
        3. repeat step2 for all elem
        """

        ans = []
        nums.sort()

        for i in range(len(nums)):
            if i >= 1 and nums[i] == nums[i-1]: continue

            start, end = i+1, len(nums)-1
            while start < end:
                cur_sum = nums[i] + nums[start] + nums[end]
                if cur_sum == 0:
                    ans.append([nums[i], nums[start], nums[end]])
                    start += 1
                    while start < len(nums) and nums[start] == nums[start-1]:
                        start += 1
                    end -= 1
                elif cur_sum > 0:
                    end -= 1
                elif cur_sum < 0:
                    start += 1
        
        return ans
            

