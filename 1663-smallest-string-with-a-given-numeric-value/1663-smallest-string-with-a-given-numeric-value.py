class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result=['a']*n
        k-=n

        i=n-1
        while k>0:
            num=min(25, k)
            result[i]=chr(ord('a')+num)
            k-=num
            i-=1
        
        return ''.join(result)