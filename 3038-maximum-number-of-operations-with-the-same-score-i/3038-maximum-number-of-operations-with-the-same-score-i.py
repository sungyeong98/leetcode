class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        result=0
        prev=None
        while len(nums)>1:
            n1=nums.pop(0)
            n2=nums.pop(0)
            if prev is None:
                result+=1
                prev=n1+n2
            elif prev==n1+n2:
                result+=1
            else:
                break
        return result