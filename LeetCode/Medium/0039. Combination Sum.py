class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]

        idea:
         - each subset can include or not include the curr elem
         - if include, add to the sum & go to next iter
         - if exclude, go straight to next iter
        """

        ans = []
        curr_comb_sum = []

        def backtrack(i, curr_sum):
            if i >= len(candidates) or curr_sum > target:
                return
            elif curr_sum == target:
                ans.append(list(curr_comb_sum))
                return
            
            # combination including candidates[i]
            curr_comb_sum.append(candidates[i])
            backtrack(i, curr_sum + candidates[i])

            # combination not including candidates[i]
            curr_comb_sum.pop()
            backtrack(i+1, curr_sum)
        
        backtrack(0, 0)
        return ans
            

        
