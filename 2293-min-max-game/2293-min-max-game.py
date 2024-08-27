class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        n=len(nums)

        while n>1:
            temp=[]
            for i in range(0,n,2):
                sub=nums[i:i+2]
                if (i//2)%2==0:
                    temp.append(min(sub))
                else:
                    temp.append(max(sub))
            
            nums=temp
            n=len(nums)
        
        return nums[0]