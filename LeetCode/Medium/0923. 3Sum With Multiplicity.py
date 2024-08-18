class Solution(object):
    def threeSumMulti(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        arr.sort()
        ans = 0
        arr_map = {}
        for n in arr: arr_map[n] = arr_map.get(n, 0) + 1

        i = 0
        while i < len(arr):
            l, r = i, len(arr)-1
            while l < r:
                if arr[i] + arr[l] + arr[r] < target:
                    l += arr_map[arr[l]]
                elif arr[i] + arr[l] + arr[r] > target:
                    r -= arr_map[arr[r]]
                else:
                    if arr[i] != arr[l] != arr[r]:
                        ans += arr_map[arr[i]] * arr_map[arr[l]] * arr_map[arr[r]]
                    elif arr[i] == arr[l] != arr[r]:
                        ans += (arr_map[arr[i]] * (arr_map[arr[i]]-1) / 2) * arr_map[arr[r]]
                    elif arr[i] != arr[l] == arr[r]:
                        ans += arr_map[arr[i]] * (arr_map[arr[l]] * (arr_map[arr[l]]-1) / 2)
                    else:
                        ans += arr_map[arr[i]] * (arr_map[arr[i]]-1) * (arr_map[arr[i]]-2) / 6
                    l += arr_map[arr[l]]
                    r -= arr_map[arr[r]]
            i += arr_map[arr[i]]

        return ans % (10**9 + 7)

                    

        
