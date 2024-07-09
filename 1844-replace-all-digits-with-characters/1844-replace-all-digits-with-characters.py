class Solution:
    def replaceDigits(self, s: str) -> str:
        result=''
        s=list(s)
        for i in range(0,len(s)-1,2):
            word=s[i]
            move=int(s[i+1])
            result+=word
            result+=chr(ord(word)+move)
        if len(s)%2==1:
            result+=s[-1]
        return result