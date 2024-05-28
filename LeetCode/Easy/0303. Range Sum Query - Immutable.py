class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        acc = 0
        for i in range(len(nums)):
            nums[i] += acc
            acc = nums[i]
        self.sums = nums
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.sums[right] - (self.sums[left-1] if left-1 >= 0 else 0)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
