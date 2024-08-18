class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        ans = 0
        songs = {}
        for t in time:
            t %= 60

            if 60-t in songs: ans += songs[60-t]
            if t == 0: ans += songs.get(0, 0)

            songs[t] = songs.get(t, 0) + 1
        
        return ans

        

        
