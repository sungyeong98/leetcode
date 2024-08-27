class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd=sorted([val for idx,val in enumerate(nums) if idx%2==1],reverse=True)
        even=sorted([val for idx,val in enumerate(nums) if idx%2==0])

        result=[]
        for e,o in zip_longest(even,odd,fillvalue=None):
            if e!=None:
                result.append(e)
            if o!=None:
                result.append(o)
        return result