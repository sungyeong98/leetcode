class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        result=[]
        for i in list(zip(*grid)):
            temp=list(map(str,i))
            temp.sort(reverse=True, key=lambda x:len(x))
            result.append(len(temp[0]))
        return result