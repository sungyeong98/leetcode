class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        num=[1 if i%2==1 else 0 for i in nums]

        left,right=0,0
        result=0
        temp=0
        while right<len(num):
            temp+=num[right]    
            right+=1

            while temp>k:
                temp-=num[left]
                left+=1
            
            if temp==k:
                t=left
                while t<right and num[t]==0:
                    t+=1
                result+=t-left+1
        return result