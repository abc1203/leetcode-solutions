class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        idea:
         - for each iter i, use nums[i] as 1st elem
         - take the remaining elems to get the remaining perms
        """

        if len(nums) == 1: return [nums]

        ans = []
        for i in range(len(nums)):
            new_nums = nums[:i] + nums[i+1:]
            remaining_perms = self.permute(new_nums)

            for perm in remaining_perms:
                ans.append([nums[i]] + perm)
        
        return ans



        
