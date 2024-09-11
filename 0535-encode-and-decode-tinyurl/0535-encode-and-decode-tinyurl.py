import hashlib
class Codec:
    def __init__(self):
        self.urls={}

    def hash(self, s):
        return 'https://tin.e/'+hashlib.md5(s.encode()).hexdigest()

    def encode(self, longUrl: str) -> str:
        hash_key=self.hash(longUrl)
        self.urls[hash_key]=longUrl
        return hash_key

    def decode(self, shortUrl: str) -> str:
        return self.urls[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))