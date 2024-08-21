class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n=len(nums)
        temp=deque([nums[i+1]-nums[i] for i in range(n-1)])
        cnt=[0]*n
        for i in range(2,n):
            cnt[i]=cnt[i-1]+(i-1)
        result=0

        stack=[]
        while temp:
            if not stack:
                stack.append(temp.popleft())
            else:
                if stack[-1]==temp[0]:
                    stack.append(temp.popleft())
                else:
                    result+=cnt[len(stack)]
                    stack=[temp.popleft()]
        if len(stack)>1:
            result+=cnt[len(stack)]
        return result