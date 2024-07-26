class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even=[i for i in nums if i%2==0]
        odd=[i for i in nums if i%2==1]
        result=[]
        for e,o in zip(even, odd):
            result.append(e)
            result.append(o)
        return result