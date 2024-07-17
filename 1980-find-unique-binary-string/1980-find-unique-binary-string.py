class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        #solution1
        '''
        n=len(nums[0])
        temp=[]
        for i in range(2**n):
            num=bin(i)[2:]
            if len(num)<n:
                num='0'*(n-len(num))+num
            temp.append(num)
        result=list(set(temp)-set(nums))
        return result[0]
        '''

        #solution2
        n=len(nums[0])
        nums=[int(i,2) for i in nums]
        num=[i for i in range(2**n)]
        temp=list(set(num)-set(nums))
        result=bin(temp[-1])[2:]
        return '0'*(n-len(result))+result