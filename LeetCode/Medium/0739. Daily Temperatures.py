class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]

        idea:
        use a stack & track the index
        while new temp > stack.top, pop stack.top; find diff for popped elem
        when new temp <= stack.top, push new temp
        """

        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                old_ind = stack.pop() # warmer day has been found for old day
                ans[old_ind] = i - old_ind
            
            stack.append(i)
        
        return ans
        
