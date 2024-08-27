class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        temp=[]
        for i in nums:
            if not temp or temp[-1]!=i:
                temp.append(i)
        n=len(temp)
        result=0
        for i in range(1,n-1):
            left,cur,right=temp[i-1],temp[i],temp[i+1]
            if (cur>left and cur>right) or (cur<left and cur<right):
                result+=1
        return result