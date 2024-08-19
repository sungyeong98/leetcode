class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        result=0
        prev=0
        for upper, percent in brackets:
            if prev<income:
                temp=min(income, upper) - prev
                result+=temp*percent/100
                prev=upper
            else:
                break
        return result