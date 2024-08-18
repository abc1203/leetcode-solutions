class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        ans = 0
        oneTwo = {}
        for n1 in nums1:
            for n2 in nums2:
                oneTwo[n1+n2] = oneTwo.get(n1+n2, 0) + 1
        for n3 in nums3:
            for n4 in nums4:
                ans += oneTwo.get(-(n3+n4), 0)

        return ans
        
