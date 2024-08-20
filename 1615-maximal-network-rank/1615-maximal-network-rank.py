class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degree=[0]*n
        for x,y in roads:
            degree[x]+=1
            degree[y]+=1

        road_set=set(tuple(i) for i in roads)
        result=0

        for i in range(n):
            for j in range(i+1, n):
                rank=degree[i]+degree[j]
                if (i,j) in road_set or (j,i) in road_set:
                    rank-=1
                result=max(result,rank)
        
        return result