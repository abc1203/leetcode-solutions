class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        idea:
        sol 1
            1. create key-value pairs of (num, freq)
            2. put all of these into a max heap based on the frequency
            3. pop the max heap k times
        
        sol 2 - O(nlogn)
            1. create a hashmap with nums & their frequency
            2. sort the hashmap by value
            3. extract top k elements in hashmap
        """

        # create hashmap with according frequencies
        num_map = {}
        for i in nums:
            if i in num_map:
                num_map[i] += 1
            else:
                num_map[i] = 1
        
        # sort hashmap by value
        ordered_dict = dict(sorted(num_map.items(), key = lambda item: item[1]))

        # get top k elements
        res = list(ordered_dict.keys())
        return res[len(res)-k:]
        

        
