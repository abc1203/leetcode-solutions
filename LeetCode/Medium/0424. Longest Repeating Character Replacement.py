class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int

        algo:
        1. use two pointers l and r
        2. keep track of count of most frequent char between l and r; this value can only increases with a new char that appears more than last time
        3. if there are more than k chars different from the most frequent, increment l until there are less than k chars different from the most frequent
        4. for each iteration, check if the new l & r creates longer substring than before
        """

        ans = 0
        max_freq = 0
        l = 0
        mp = {}

        for r in range(len(s)):
            if s[r] not in mp:
                mp[s[r]] = 1
            else:
                mp[s[r]] += 1
            
            max_freq = max(max_freq, mp[s[r]])

            while (r - l + 1) - max_freq > k:
                mp[s[l]] -= 1
                l += 1
            
            ans = max(ans, r - l + 1)
            
        return ans


