from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        temp=defaultdict(list)

        for i,j in edges:
            temp[i].append(j)
            temp[j].append(i)

        return max(temp, key=lambda x:len(temp[x]))