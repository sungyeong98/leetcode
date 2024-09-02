class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n=len(nums)
        result=[False]*n
        for i in range(1,n+1):
            temp=''.join(list(map(str,nums[:i])))
            if int(temp,2)%5==0:
                result[i-1]=True
        return result