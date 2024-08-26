class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        result=''
        for idx, num in enumerate(map(lambda x:ord(x)-97,s)):
            dis=min(num,26-num)
            if dis<=k:
                k-=dis
                result+='a'
            else:
                result+=chr(num+97-k)
                break
        return result+s[idx+1:]