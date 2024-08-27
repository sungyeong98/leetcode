class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result=0
        stack=[]
        for i in nums:
            if not stack or stack[-1]<i:
                stack.append(i)
            else:
                result=max(result,sum(stack))
                stack=[i]
        result=max(result,sum(stack))
        return result