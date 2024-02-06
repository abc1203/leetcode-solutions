class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        idea (greedy + bin search O(nlogn))
         - keep track of a current subsequence
         - when the new elem can't fit in current subseq, replace using the new elem
         - and insert into its appropriate pos in the old subseq
        """

        subseq = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] > subseq[-1]: subseq.append(nums[i])
            else:
                l, r = 0, len(subseq)-1
                i_ind = l
                while l <= r:
                    mid = (l+r) / 2
                    if subseq[mid] >= nums[i]: r = mid - 1
                    else: 
                        l = mid + 1
                        i_ind = l

                # replace
                subseq[i_ind] = nums[i]

        return len(subseq)



        
