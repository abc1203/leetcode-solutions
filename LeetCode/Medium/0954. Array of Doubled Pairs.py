class Solution(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        arr_map = {}
        for n in arr: arr_map[n] = arr_map.get(n, 0) + 1

        sorted_arr = arr_map.keys()
        sorted_arr.sort(key=abs)

        for n in sorted_arr:
            if n in arr_map and 2*n in arr_map:
                cnt = arr_map[n]
                arr_map[2*n] -= cnt
                if arr_map[2*n] == 0: del arr_map[2*n]
                elif arr_map[2*n] < 0: return False

                if n in arr_map: del arr_map[n]  
            elif n in arr_map:
                return False
        
        return True
            
        
