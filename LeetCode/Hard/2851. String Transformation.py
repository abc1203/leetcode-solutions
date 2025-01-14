class Solution(object):
    def numberOfWays(self, s, t, k):
        """
        :type s: str
        :type t: str
        :type k: int
        :rtype: int

        s = abcd
        t = cdab
        i = 0: abcd
        i = 1: bcda
        i = 2: cdab
        i = 3: dabc
        abcdabcd

         - enumerate each index as the beginning index
         - for each possible rotation/index, use KMP to find the good indices == t
        METHOD 1:
         - dp[i][j] = # of ways to obtain s'=s[i] as start in j steps
         - dp[i][j] = Summ(dp[k][j-1]) for k noteq i
         - finally add the good indices with Summ(dp[good i][k])
         - doing this directly doesn't work bc k very large, so find patterns
         - note that at the kth step , sum = (n-1)^k = f_k(i=0) + (n-1) * f_k(i=/=0)
         - f_k(i=0) - f_k(i=/=0) = (-1)^k
         - so f_k(i=/=0) = ((n-1)^k - (-1)^k) / n
         - now use fast power algo to calculate exponents
        METHOD 2:
         - we can separate into i=0 and i noteq 0
         - dp[t][i=0/1] = # of ways to get i=0 and i noteq 0 after t steps
         - dp[t][0] = dp[t-1][1] * (n-1)
         - dp[t][1] = dp[t-1][0] + dp[t-1][1] * (n-2)
         - then use matrix multiplication + power of matrices to get res
        """
        
        def kmp(s, pat):
            n = len(pat)
            lps = [0] * n
            res = []
            for i in range(1, n):
                j = lps[i - 1]
                while j > 0 and pat[i] != pat[j]: j = lps[j - 1]
                if j == 0 and pat[0] != pat[i]: lps[i] = 0
                else: lps[i] = j + 1
            j = 0
            for i in range(len(s)):
                while j >= n or j > 0 and s[i] != pat[j]: j = lps[j - 1]
                if s[i] == pat[j]: j += 1
                if j == n: res.append(i - n + 1)
            return res
        
        n, M = len(s), 10**9+7
        ans = 0
        good_indices = kmp((s+s)[:-1], t)

        ans_k = [0, 0]
        ans_k[1] = (pow(n-1, k, M) - (-1)**k + M) * pow(n, M-2, M) % M
        ans_k[0] = (ans_k[1] + (-1)**k + M) % M
        for ind in good_indices:
            if ind == 0: ans += ans_k[0]
            else: ans += ans_k[1]
            ans %= M
        return ans % M

