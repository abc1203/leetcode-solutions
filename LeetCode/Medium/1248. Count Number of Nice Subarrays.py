class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt = {} # number of even numbers before each odd num
        oddIdx = []
        evenCnt = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                cnt[i] = evenCnt+1
                evenCnt = 0
                oddIdx.append(i)
            else:
                evenCnt += 1
        cnt[len(nums)] = evenCnt+1
        oddIdx.append(len(nums))
        
        l,r = 0,0
        ans = 0
        while r < len(oddIdx)-1:
            if r - l + 1 == k:
                ans += cnt[oddIdx[r+1]] * cnt[oddIdx[l]]
                l += 1
            r += 1
        return ans


        

        
        
