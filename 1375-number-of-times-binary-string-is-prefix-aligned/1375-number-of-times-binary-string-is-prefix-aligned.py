class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        temp=accumulate(flips,max)
        result=0
        for idx,val in enumerate(temp,1):
            if idx==val:
                result+=1
        return result