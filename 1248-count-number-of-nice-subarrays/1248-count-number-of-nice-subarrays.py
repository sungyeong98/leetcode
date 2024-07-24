class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        result=0
        temp=[]
        for i in nums:
            if i%2==1:
                temp.append(1)
            else:
                temp.append(0)
        
        left,right=0,1
        while left<right:
            if sum(temp[left:right])==k:
                result+=1
            else:
                left