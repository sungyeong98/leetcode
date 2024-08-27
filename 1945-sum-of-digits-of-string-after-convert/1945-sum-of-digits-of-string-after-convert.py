class Solution:
    def getLucky(self, s: str, k: int) -> int:
        result=''.join([str(ord(i)-ord('a')+1) for i in s])
        while k>0:
            temp=0
            for i in result:
                temp+=int(i)
            result=str(temp)
            k-=1
        return result