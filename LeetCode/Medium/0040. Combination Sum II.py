class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]

        idea:
         - sort nums first to avoid duplicates
         - to include, add it to curr_comb_sum
         - to exclude, go straight to the next different num in candidates
        """

        ans = []
        curr_comb_sum = []
        candidates.sort()

        def iterate(i, curr_sum):
            if curr_sum == target:
                ans.append(list(curr_comb_sum))
                return
            elif curr_sum > target or i >= len(candidates): return
            
            # include candidate[i]
            curr_comb_sum.append(candidates[i])
            iterate(i+1, curr_sum + candidates[i])

            # exclude candidates[i]
            curr_comb_sum.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]: i += 1
            iterate(i+1, curr_sum)
        
        iterate(0, 0)
        return ans
        
