class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        ans = 0
        words_map = {}

        for word in words:
            if word[::-1] in words_map: 
                ans += 4
                words_map[word[::-1]] -= 1
                if words_map[word[::-1]] == 0: del words_map[word[::-1]]
            else:
                words_map[word] = words_map.get(word, 0) + 1
        
        for word in words_map.keys():
            if word[0] == word[1]:
                ans += 2
                break
        return ans
            



        
