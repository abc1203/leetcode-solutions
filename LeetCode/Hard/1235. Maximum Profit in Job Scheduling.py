class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int

         - sort jobs by end time 1-n
         - check the end time for each job using dp
         - dp[i] = max profit for jobs 1 to i
             = max(dp[i-1], dp[start time for ith job] + profit for ith job)
         - use bin search to find correct idx
         - O(NlogN) time, O(N) space
        """

        def bin_search(rightmost, new_start_time):
            l, r = 0, rightmost
            while l <= r:
                m = (l + r) / 2
                if 0 <= m < rightmost-1 and data[m][1] <= new_start_time < data[m+1][1]:
                    return m
                elif 0 <= m < rightmost and new_start_time < data[m][1]:
                    r = m - 1
                else:
                    l = m + 1
            return r

        data = sorted(zip(startTime, endTime, profit), key = lambda x : x[1])
        n = len(data)
        dp = [0] * n
        dp[0] = data[0][2]

        for i in range(1, n):
            if data[i][0] >= data[i-1][1]: # new start time >= old end time
                dp[i] = dp[i-1] + data[i][2]
            else:
                # find appropriate idx based on new start time
                j = bin_search(i, data[i][0])

                if j < 0: dp[i] = max(dp[i-1], data[i][2])
                else: dp[i] = max(dp[i-1], dp[j] + data[i][2])
        return dp[n-1]
