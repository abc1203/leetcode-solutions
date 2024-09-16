class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int

         - same as two sum except target is any value with power of 2
         - just check all powers of 2 with each num
        """

        cnt = {}
        ans = 0

        for n in deliciousness:
            # goes to 22 bc max is 2^20
            for i in range(22):
                if 2**i - n in cnt: ans += cnt[2**i - n]
            cnt[n] = cnt.get(n, 0) + 1
        return ans % (10**9+7)


        
