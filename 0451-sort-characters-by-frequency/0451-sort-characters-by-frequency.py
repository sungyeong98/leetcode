class Solution:
    def frequencySort(self, s: str) -> str:
        temp=sorted(Counter(s).items(),key=lambda x:(-x[1],x[0]))
        result=''        
        for char,cnt in temp:
            result+=char*cnt
        return result