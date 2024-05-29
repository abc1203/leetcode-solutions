class Codec:
    def __init__(self):
        self.idx = 0
        self.base = "http://tinyurl.com/"
        self.encodeMap = {}
        self.decodeMap = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        shortUrl = self.base + str(self.idx)
        self.encodeMap[longUrl] = shortUrl
        self.decodeMap[shortUrl] = longUrl
        self.idx += 1
        return shortUrl
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.decodeMap[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
