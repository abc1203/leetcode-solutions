class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        O(nlogn) sol: sort & check if elements are consceutive

        O(n) algo (at most 2n lookups):
        1. convert nums to a set s.t. we get no duplicates & O(1) search
        2. get the 1st element of set, say n
        3. find the smallest element in consecutive sequence containing n
        4. iterate through consec seq & delete all elems in it; record len
        5. repeat until no elem left in set
        """
        nums_set = set(nums)
        max_seq_len = 0

        while len(nums_set) != 0:
            # find smallest element in consecutive sequence containing num
            curr = next(iter(nums_set))
            while (curr-1) in nums_set: curr -= 1

            # iterate through found consecutive sequence & delete elems in it
            seq_len = 0
            while curr in nums_set:
                seq_len += 1
                nums_set.remove(curr)
                curr += 1

            # check if most recent sequence has greater length
            if seq_len > max_seq_len: 
                max_seq_len = seq_len
        
        return max_seq_len

        
