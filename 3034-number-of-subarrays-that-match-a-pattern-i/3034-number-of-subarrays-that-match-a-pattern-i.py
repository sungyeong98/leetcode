class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n=len(nums)
        m=len(pattern)+1
        result=0

        for i in range(n-m+1):
            temp=nums[i:i+m]
            flag=True
            for j in range(len(temp)-1):
                if pattern[j]==1 and temp[j+1]>temp[j]:
                    continue
                elif pattern[j]==0 and temp[j+1]==temp[j]:
                    continue
                elif pattern[j]==-1 and temp[j+1]<temp[j]:
                    continue
                else:
                    flag=False
                    break
            if flag:
                result+=1
        
        return result