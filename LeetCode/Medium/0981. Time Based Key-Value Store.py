class TimeMap(object):

    def __init__(self):
        self.mp = collections.defaultdict(list)
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None

        idea:
        use a hashmap with key=key and value = list of (timestamp, value)
        since timestamp incr, the list will be sorted according to time
        """
        self.mp[key].append((timestamp, value))
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str

        idea:
        use binary search with l & r
        calculate mid and compare that with timestamp
        """

        ans = ""
        l, r = 0, len(self.mp[key])-1

        while l <= r:
            mid = (l + r) / 2

            if self.mp[key][mid][0] <= timestamp:
                ans = self.mp[key][mid][1]
                l = mid + 1
            else:
                r = mid - 1
        
        return ans
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
