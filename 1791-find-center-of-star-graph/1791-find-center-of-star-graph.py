from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        temp=defaultdict(list)
        for i,j in edges:
            temp[i].append(j)
            temp[j].append(i)
        temp_dict=dict(sorted(temp.items(), reverse=True, key=lambda x:len(x[1])))

        return list(temp_dict.keys())[0]