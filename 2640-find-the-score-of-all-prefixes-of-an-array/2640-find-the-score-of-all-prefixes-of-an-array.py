class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        conver=[]
        result=[]
        max_num=0
        for i in range(len(nums)):
            max_num=max(max_num,nums[i])
            conver.append(nums[i]+max_num)
            if not result:
                result.append(conver[-1])
            else:
                result.append(result[-1]+conver[-1])
        return result