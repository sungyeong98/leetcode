class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        temp={'m':[0,0], 'p':[0,0], 'g':[0,0]}
        for i in range(len(garbage)):
            for j in list(garbage[i]):
                if j=='M':
                    temp['m'][0]+=1
                    temp['m'][1]=i
                if j=='P':
                    temp['p'][0]+=1
                    temp['p'][1]=i
                if j=='G':
                    temp['g'][0]+=1
                    temp['g'][1]=i
        result=0
        for i in temp:
            if temp[i][0]==0:
                continue
            else:
                result+=temp[i][0]
                result+=sum(travel[:temp[i][1]])
        return result
            