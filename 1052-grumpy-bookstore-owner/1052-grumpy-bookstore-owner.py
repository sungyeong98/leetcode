class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        result, temp, temp_ = 0, 0, 0
        for i in range(len(customers)):
            if grumpy[i]==0:
                result+=customers[i]
            if grumpy[i]==1:
                temp+=customers[i]

            if i>=minutes:
                if grumpy[i-minutes]==1:
                    temp-=customers[i-minutes]
            
            temp_=max(temp_,temp)
        
        return result+temp_