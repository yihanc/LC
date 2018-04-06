# 535. Encode and Decode TinyURL
# DescriptionHintsSubmissionsDiscussSolution
# Note: This is a companion problem to the System Design problem: Design TinyURL.
# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.
# 
# Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
# 
# Seen this question in a real interview before?  
# 

# 2018.03.10

class Codec:
    def __init__(self):
        self.shortToLong = {}
        self.longToShort = {}
        self.id = 1

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.longToShort:
            return "http://www.tinyurl.com/" + self.longToShort[longUrl]
        else:
            self.id += 1
            key = str(hex(self.id))
            self.longToShort[longUrl] = key
            self.shortToLong[key] = longUrl
            return "http://www.tinyurl.com/" + key
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        key = shortUrl.split("http://www.tinyurl.com/")[1]
        return self.shortToLong[key]

