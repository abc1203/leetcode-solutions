class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        n = len(adjacentPairs) + 1
        nums_pairs = {}

        for a, b in adjacentPairs:
            if a not in nums_pairs: nums_pairs[a] = [b]
            else: nums_pairs[a] += [b]
            
            if b not in nums_pairs: nums_pairs[b] = [a]
            else: nums_pairs[b] += [a]
        
        for k, v in nums_pairs.items():
            if len(v) == 1:
                start = k
                break
        
        ans = []
        curr, prev = start, None
        for i in range(n):
            ans.append(curr)
            adjac = nums_pairs[curr]
            if len(adjac) == 1:
                curr, prev = adjac[0], start
            elif adjac[0] == prev:
                prev = curr
                curr = adjac[1]
            else:
                prev = curr
                curr = adjac[0]

        return ans
                

        


        
