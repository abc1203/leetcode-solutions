class Codec:
    """
    idea:
     - use a hashmap with i as key and strs[i] as val
     - encode will become "0.1.2...n"
     - decode will get the values from hmap
    """
    def __init__(self):
        self.hmap = {}

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for i in range(len(strs)):
            self.hmap[i] = strs[i]
            res += str(i) + "."
        return res
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        res = []
        l = 0
        for i in range(len(s)):
            if s[i] == ".":
                k = int(s[l:i])
                res.append(self.hmap[k])
                l = i+1
        return res
        


    
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
