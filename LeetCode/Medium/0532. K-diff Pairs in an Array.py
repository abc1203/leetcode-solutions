class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        ans_set = set()
        ns = set(nums)

        if k != 0:
            for n in ns:
                if n+k in ns and (n,n+k) not in ans_set and (n+k,n) not in ans_set:
                    ans_set.add((n,n+k))
                if n-k in ns and (n,n-k) not in ans_set and (n-k,n) not in ans_set:
                    ans_set.add((n,n-k))
            return len(ans_set)
        else:
            for n in ns: nums.remove(n)
            return len(set(nums))




        
