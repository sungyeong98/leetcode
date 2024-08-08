class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n=len(capacity)
        temp=[capacity[i]-rocks[i] for i in range(n)]
        temp.sort()
        for i in range(n):
            if temp[i]>0:
                cnt=temp[i]
                if additionalRocks>=cnt:
                    additionalRocks-=cnt
                    temp[i]-=cnt
                else:
                    break
        return temp.count(0)