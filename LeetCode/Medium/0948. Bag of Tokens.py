class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """

        tokens.sort()

        l, r = 0, len(tokens)-1
        ans, score = 0, 0
        while l <= r:
            if power >= tokens[l]: 
                power -= tokens[l]
                score += 1
                l += 1
                ans = max(ans, score)
            elif score >= 1:
                power += tokens[r]
                score -= 1
                r -= 1
            else: break
        return ans
            
        
