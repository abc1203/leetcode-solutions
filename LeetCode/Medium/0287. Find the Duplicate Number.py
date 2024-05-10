class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        approach O(n) space: hashset
        approach O(1) space: tortoise and hare
         - after the ptrs meet, reset the slow ptr to the start and move both ptrs
            at the same pace until they meet again; meeting point is the duplicate number
         - in this case the values of the arr are the pointers
            => moving to the next is nums[slow]
        """

        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast: break
        
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]

            if slow == fast: return slow
        
