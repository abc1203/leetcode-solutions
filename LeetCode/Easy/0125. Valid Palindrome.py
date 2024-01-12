class Solution(object):
    def isAlphaNumeric(self, c):
        if ((ord(c) >= ord('a') and ord(c) <= ord('z')) or 
        (ord(c) >= ord('A') and ord(c) <= ord('Z')) or
        (ord(c) >= ord('0') and ord(c) <= ord('9'))):
            return True
        return False
    
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool

        algo:
        1. use 2 pointers - 1 from beginning & 1 from end
        2. skip non-alphanumeric indices
        """
        
        start, end = 0, len(s)-1
        while start < end:
            if not self.isAlphaNumeric(s[start]): start += 1
            elif not self.isAlphaNumeric(s[end]): end -= 1
            else:
                if s[start].lower() != s[end].lower(): return False
                start += 1
                end -= 1
        
        return True

        
