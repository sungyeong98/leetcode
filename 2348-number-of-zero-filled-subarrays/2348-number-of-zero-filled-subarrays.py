class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        zero_idx=[idx for idx,val in enumerate(nums) if val==0]
        if not zero_idx:    return 0
        start,end=zero_idx[0],zero_idx[-1]

        def count(n):
            temp=0
            for i in range(1,n+1):
                temp+=i
            return temp

        result=0
        cnt=0
        for i in range(start,end+1):
            if nums[i]==0:
                cnt+=1
            else:
                result+=count(cnt)
                cnt=0
        if cnt:
            result+=count(cnt)
        return result