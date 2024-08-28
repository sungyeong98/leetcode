class Solution:
    def countElements(self, nums: List[int]) -> int:
        c=Counter(nums)
        num=sorted(set(nums))
        n=len(num)
        result=0
        for i in range(1,n-1):
            if num[i-1]<num[i]<num[i+1]:
                result+=c[num[i]]
        return result