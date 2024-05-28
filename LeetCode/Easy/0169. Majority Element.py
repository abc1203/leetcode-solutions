class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        approach (O(1) space):
         - Moore's voting algo
         - set 1st elem as majority elem (candidate)
         - incr count when curr elem == candidate; else decrease
         - if count is zero, switch candidate
        """

        count, candidate = 0, 0
        for n in nums:
            if count == 0:
                candidate = n
            count += 1 if n == candidate else -1
        return candidate
        
