class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        idea2:
        1. define l & r first and check if nums[mid] == target
        2. if not, we have 2 cases:
            a. nums[mid] >= nums[l] - in this case we have:
                target > nums[mid] or target < nums[l] => target in right half => l = mid + 1
                else r = mid -1
            b. nums[mid] < nums[l] - in this case we have:
                target > nums[mid] and target < nums[l] => target in right half
        """

        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) / 2
            
            if nums[mid] == target: return mid
            elif nums[mid] >= nums[l]: 
                if target > nums[mid] or target < nums[l]: # in right half
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[mid] < nums[l]:
                if target > nums[mid] and target < nums[l]: # in right half
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1

        
