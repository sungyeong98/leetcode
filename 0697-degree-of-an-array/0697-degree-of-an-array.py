class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        c=Counter(nums)
        num_idx=defaultdict(list)
        target=[i for i in c.keys() if c[i]==max(c.values())]
        result=float('inf')
        for idx,val in enumerate(nums):
            num_idx[val].append(idx)

        for num in target:
            result=min(result,num_idx[num][-1]-num_idx[num][0]+1)
        return result