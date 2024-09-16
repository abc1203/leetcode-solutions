class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allowed_char = set(allowed)
        ans = 0

        for word in words:
            is_allowed = True
            for c in word:
                if c not in allowed_char: 
                    is_allowed = False
                    break
            if is_allowed: ans += 1
        return ans
        
