class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        idx=list(filter(lambda i:nums[i]==x, range(len(nums))))
        result=[]
        for num,cnt in zip(nums,queries):
            if num==x:
                if len(idx)>=cnt:
                    result.append(idx[cnt-1])
            else:
                result.append(-1)
        return result
