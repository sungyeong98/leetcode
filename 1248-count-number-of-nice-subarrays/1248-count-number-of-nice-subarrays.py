class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        #solution1
        '''
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
        '''

        #solution2
        n=len(nums)
        q=[]
        for i in range(n):
            if nums[i]&1:
                q.append(i)
        q=[-1]+q+[n]

        return sum((q[i]-q[i-1])*(q[i+k]-q[i+k-1]) for i in range(1,len(q)-k))