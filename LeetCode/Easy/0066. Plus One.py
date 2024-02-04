class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        l = []
        for i in range(0, len(digits)):
            num = 10 * num
            num = num + digits[i]
        print(num)
        num = num + 1

        while num != 0:
            digit = num % 10

            num = num / 10
            l.append(digit)
        l.reverse()
        print(l)
        return l
      
