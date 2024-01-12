class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        O(n) algo (efficient):
        1. convert nums to a set s.t. we get no duplicates & O(1) search
        2. get the 1st element of set, say n
        3. check if n is the 1st element in consec seq
        4. if it is, iterate & get len of seq
        """
        nums_set = set(nums)
        max_seq_len = 0

        for num in nums_set:
            seq_len = 0
            if (num-1) not in nums_set:
                curr = num
                while curr in nums_set: 
                    seq_len += 1
                    curr += 1
            
            if seq_len > max_seq_len: max_seq_len = seq_len
        
        return max_seq_len

        
