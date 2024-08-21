class Solution:
    def printVertically(self, s: str) -> List[str]:
        s=s.split(' ')
        result=[]
        for i in list(zip_longest(*s, fillvalue=' ')):
            temp=list(i)
            while temp[-1]==' ':
                temp.pop()
            result.append(''.join(temp))
        return result