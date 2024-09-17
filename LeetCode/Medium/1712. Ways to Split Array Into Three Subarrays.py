class Solution(object):
    def waysToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
         - two ptr
         - use prefix sums to get sum in O(1)
         - for each iter, find possible range of the mid subarr using j & k
         - note that j & k can only increase as i increases => O(n)
        """
        n, total = len(nums), sum(nums)
        ans = 0

        f, f_sum = [0]*n, 0
        for i in range(n):
            f_sum += nums[i]
            f[i] = f_sum

        j, k = 0, 0
        for i in range(n-2):
            while j <= i or (j < n-1 and f[j] < f[i]*2): # find min possible
                j += 1
            while k < j or (k < n-1 and f[k] - f[i] <= f[-1] - f[k]): # find max possible
                k += 1
            ans += (k - j)
        return ans % (10**9+7)



        
