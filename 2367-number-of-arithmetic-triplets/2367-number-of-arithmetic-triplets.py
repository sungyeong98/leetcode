class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        temp=[]
        for i in range(len(nums)-1):
            for j in range(i,len(nums)):
                if nums[j]-nums[i]==diff:
                    temp.append((i,j))
        result=0
        for i in range(len(temp)-1):
            for j in range(i+1,len(temp)):
                if temp[i][1]==temp[j][0]:
                    result+=1
        return result