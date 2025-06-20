    class Codec:

        #for each URL generate a unique ID and put it in a hash map

        def __init__(self):
            self.count=1
            self.long_to_short={}
            self.short_to_long={}
        
        def encode(self, longUrl: str) -> str:
            """Encodes a URL to a shortened URL.
            """
            if longUrl in self.long_to_short:
                return self.long_to_short[longUrl]
            
            shortUrl= str(self.count)
            self.long_to_short[longUrl]=shortUrl
            self.short_to_long[shortUrl]=longUrl
            self.count+=1

            return shortUrl
            

        def decode(self, shortUrl: str) -> str:
            """Decodes a shortened URL to its original URL.
            """

            return self.short_to_long[shortUrl]
    
        
            
    #time complexity O(1)
    #space complexity O(k*N), k is the average length of a URL

    # Your Codec object will be instantiated and called as such:
    # codec = Codec()
    # codec.decode(codec.encode(url))