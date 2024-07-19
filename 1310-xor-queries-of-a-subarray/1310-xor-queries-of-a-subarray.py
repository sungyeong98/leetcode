class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        result=[]
        temp=list(accumulate(arr,lambda x,y:x^y))

        for s,e in queries:
            if s==0:
                result.append(temp[e])
            else:
                result.append(temp[e]^temp[s-1])
        
        return result