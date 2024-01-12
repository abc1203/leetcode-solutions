class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]

        algo:
        1. use 2 pointers - one from start & one from end
        2. if n[start] + n[end] < target: start++
        3. if n[start] + n[end] > target: end--
        """

        start, end = 0, len(numbers)-1

        while start < end:
            if numbers[start] + numbers[end] == target: 
                return [start+1, end+1]
            elif numbers[start] + numbers[end] < target:
                start += 1
            elif numbers[start] + numbers[end] > target:
                end -= 1

        
