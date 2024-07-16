class Solution:
    def minTimeToType(self, word: str) -> int:
        result=len(word)
        word='a'+word

        for i in range(len(word)-1):
            left,right=min(word[i],word[i+1]),max(word[i],word[i+1])
            cnt=min(ord(right)-ord(left), (ord('z')-ord(right))+(ord(left)-ord('a'))+1)
            result+=cnt
        return result