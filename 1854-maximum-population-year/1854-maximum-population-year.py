class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        temp=defaultdict(int)
        for a,b in logs:
            for y in range(a,b):
                temp[y]+=1
        return max(temp.items(), key=lambda x:(x[1],-x[0]))[0]