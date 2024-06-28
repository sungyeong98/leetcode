from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        temp=defaultdict(int)
        for i,j in edges:
            temp[i]+=1
            temp[j]+=1
        return max(temp,key=lambda x:temp[x])