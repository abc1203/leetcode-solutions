class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        idea:
        - backtrack: returns all subsets of nums[:i+1]
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
        
