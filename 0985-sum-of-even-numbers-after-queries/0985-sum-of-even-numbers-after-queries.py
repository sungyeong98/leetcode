class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result=[]
        prev=sum([i for i in nums if i%2==0])
        for val,idx in queries:
            if nums[idx]%2==0:
                temp=nums[idx]
                nums[idx]+=val
                if abs(val)%2==1:
                    prev-=temp
                else:
                    prev+=val
            else:
                nums[idx]+=val
                if abs(val)%2==1:
                    prev+=nums[idx]
            result.append(prev)
        return result