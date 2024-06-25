class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        original,result=0, 0
        dict={}
        for i in range(len(grumpy)):
            if grumpy[i]==0:
                original+=customers[i]
            else:
                dict[i]=customers[i]
                
        if len(dict)==0:
            return original

        for idx in dict:
            temp=original
            for nidx in range(idx,idx+minutes):
                if nidx in dict:
                    temp+=dict[nidx]
            
            result=max(result,temp)

        return result