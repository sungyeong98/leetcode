class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        temp={}
        for start,end in paths:
            if start not in temp:
                temp[start]=[end]
            else:
                temp[start].append(end)
            
            if end not in temp:
                temp[end]=[]
        return [i for i in temp.keys() if len(temp[i])==0][0]