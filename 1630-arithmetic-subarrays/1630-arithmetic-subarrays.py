class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result=[]
        for left,right in zip(l,r):
            num=nums[left:right+1]
            num.sort()
            flag=True
            for i in range(1,len(num)-1):
                if num[i]-num[i-1]!=num[i+1]-num[i]:
                    flag=False
                    break
            if flag:
                result.append(True)
            else:
                result.append(False)
        return result