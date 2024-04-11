class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float

        approach 1: merge and find median O(m+n)
        approach 2: 2-ptr O(m+n)
             - iterate through 2 arrays until half of the total elem are iterated
        approach 3: bin search O(logm/logn)
             1. partition the smaller arr into 2 parts
             2. find the partition of larger arry s.t. left side of partition of both arr
                is half of total elem
             3. if the partition is valid (largest left <= smallest right), return median
        """

        l, r = 0, 0
        mid = (len(nums1) + len(nums2)) / 2
        prev2, prev1 = 0, 0

        while l + r <= mid:
            prev2 = prev1

            if l < len(nums1) and r < len(nums2):
                if nums1[l] < nums2[r]: 
                    prev1 = nums1[l]
                    l += 1
                else: 
                    prev1 = nums2[r]
                    r += 1
            elif l == len(nums1): 
                prev1 = nums2[r]
                r += 1
            elif r == len(nums2): 
                prev1 = nums1[l]
                l += 1
        
        # l + r > mid
        if (len(nums1)+len(nums2)) % 2 == 0:
            return (float(prev2) + float(prev1)) / 2
        else:
            return prev1

        




        
