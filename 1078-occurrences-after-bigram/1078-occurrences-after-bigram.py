class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        t=text.split(' ')
        n=len(t)
        result=[]
        for i in range(n-2):
            if t[i]==first and t[i+1]==second:
                result.append(t[i+2])
        return result