class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        idea:
         - backtrack: returns all subsets related to nums[i]
         - each iter has 2 choice: to include or not include
         - both will continue iterating until end of nums is reached
        """
        ans = []
        curr_subset = []
        
        def backtrack(i):
            if i == len(nums): 
                ans.append(curr_subset.copy())
                return

            # subsets including nums[i]
            curr_subset.append(nums[i])
            backtrack(i+1)
            
            # subsets excluding nums[i]
            curr_subset.pop()
            backtrack(i+1)

        backtrack(0)
        return ans
        
