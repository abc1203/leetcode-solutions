class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int

        idea:
        have a set to keep track of the chars in current substr
        if a repeated char is found, drop all the chars before the repeated char
        """

        ans = 0
        starting_index = 0
        substr = set()
        for i in range(0, len(s)):
            if s[i] not in substr:
                substr.add(s[i])
            else:
                for j in range(starting_index, i):
                    if s[j] == s[i]: 
                        del_index = j
                
                for j in range(starting_index, del_index):
                    substr.remove(s[j])
                
                starting_index = del_index + 1
            
            ans = max(ans, len(substr))
        
        return ans
