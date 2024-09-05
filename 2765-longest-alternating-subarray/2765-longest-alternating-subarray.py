class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        temp=[nums[i+1]-nums[i] for i in range(n-1)]+[0]
        result=-1
        stack=[]
        for i in temp:
            if (not stack and abs(i)==1) or stack[-1]==-i:
                stack.append(i)
            else:
                result=max(result,len(stack)+1)
                stack=[i]
        return result