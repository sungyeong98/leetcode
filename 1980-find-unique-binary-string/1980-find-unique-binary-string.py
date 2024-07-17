class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums[0])
        temp=[]
        for i in range(2**n):
            num=bin(i)[2:]
            if len(num)<n:
                num='0'*(n-len(num))+num
            temp.append(num)
        result=list(set(temp)-set(nums))
        return result[0]