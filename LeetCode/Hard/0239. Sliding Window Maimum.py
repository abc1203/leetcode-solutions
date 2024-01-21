class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        idea:
        use a sliding window with l & r; use a deque that tracks index
        for each iteration (r += 1):
            1. pop the elements < current and append current (q[0] is max index)
            2. l += 1; if l > q[0], pop q[0]
        """

        ans = []
        l = 0
        q = collections.deque()
        for r in range(len(nums)):
            while len(q) > 0 and nums[r] > nums[q[-1]]: q.pop()
            q.append(r)

            if r - l + 1 >= k: 
                ans.append(nums[q[0]])

                l += 1
                if l > q[0]: q.popleft()
        
        return ans
        
