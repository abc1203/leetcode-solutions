class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        idea:
         - first solve the next greater element problem with a stack
         - while stack.top < new elem, pop stack.top; then place new elem in
         - stack stores the values
        """
        
        # nums2 value : next greater elem
        hm = {}
        s = []
        for i in range(len(nums2)):
            while len(s) > 0 and s[-1] < nums2[i]:
                top = s.pop()
                hm[top] = nums2[i]
            s.append(nums2[i])
        
        while len(s) > 0:
            top = s.pop()
            hm[top] = -1

        ans = []
        for n in nums1:
            ans.append(hm[n])
        return ans

        
