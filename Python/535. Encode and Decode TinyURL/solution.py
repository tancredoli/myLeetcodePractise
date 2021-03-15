class Codec:
    def __init__(self):
        self.hash = {}
        self.cnt = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.hash[self.cnt] = longUrl
        curr = str(self.cnt)
        self.cnt += 1
        return curr

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        key = int(shortUrl)
        return self.hash[key]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))