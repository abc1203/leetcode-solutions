class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        idea:
         - sort nums
         - 2 cases: to include nums[i] or to exclude
         - to include, add it to curr_subset
         - to exclude, check if nums[i] == nums[i+1]; if equal, skip to next iter
        """

        ans = []
        curr_subset = []

        nums.sort()

        def iterate(i):
            if i >= len(nums): 
                ans.append(list(curr_subset))
                return
            
            # include nums[i]
            curr_subset.append(nums[i])
            iterate(i+1)

            # exclude nums[i]
            curr_subset.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]: i += 1
            iterate(i+1)
        
        iterate(0)
        return ans
        
