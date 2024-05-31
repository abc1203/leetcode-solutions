class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        ans = []
        digits = "123456789"
        dLow, dHigh = len(str(low)), len(str(high))
        possible = set()

        for i in range(dLow, dHigh+1):
            for j in range(0, len(digits)-i+1):
                possible.add(int(digits[j:j+i]))
        
        for n in possible:
            if n >= low and n <= high: ans.append(n)
        ans.sort()
        return ans



        
