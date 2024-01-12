class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        O(n) algo:
        1. create a hashmap with key = num & value = frequency
        2. create an array with index = frequency & value = num
        3. select the top k elements in the array
        """

        mp = {}
        for num in nums:
            if num not in mp: 
                mp[num] = 1
            else:
                mp[num] += 1
        
        arr = [[] for i in range(0, len(nums)+1)]
        for num_val, freq in mp.items():
            arr[freq].append(num_val)
        
        ans = []
        size = 0
        for i in range(len(nums), 0, -1):
            for j in range(0, len(arr[i])):
                ans.append(arr[i][j])
                size += 1
                if size == k: return ans
        
