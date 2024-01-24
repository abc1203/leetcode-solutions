class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        idea1:
        1. find the index for minimum element
        2. by comparing the rightmost elem, check if it belongs to [nums[k], ..., nums[n-1]] or [nums[0], ..., nums[k-1]]
        3. run binary search from the subarray it belongs to
        """

        def minIndex():
            l, r = 0, len(nums)-1
            min_index = l

            while l <= r:
                mid = (l + r) / 2
                min_index = (mid if nums[mid] < nums[min_index] else min_index)

                if nums[mid] < nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            return min_index
        
        min_index = minIndex()
        add_index = False
        if nums[min_index] <= target and target <= nums[len(nums)-1]:
            nums = nums[min_index:]
            add_index = True
        else:
            nums = nums[:min_index]
        
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) / 2

            if nums[mid] == target: return (mid+min_index if add_index else mid)
            elif nums[mid] < target: l = mid + 1
            else: r = mid - 1
        
        return -1

        
