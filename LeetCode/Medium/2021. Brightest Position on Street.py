class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        brightness = {}

        for pos, ran in lights:
            l, r = pos - ran, pos + ran
            brightness[l] = brightness.get(l, 0) + 1
            brightness[r+1] = brightness.get(r+1, 0) - 1
        
        ans, curr_max, curr_brightness = -1, 0, 0
        for idx, val in sorted(brightness.items()):
            curr_brightness += val
            if curr_brightness > curr_max:
                curr_max = curr_brightness
                ans = idx
        return ans

        

