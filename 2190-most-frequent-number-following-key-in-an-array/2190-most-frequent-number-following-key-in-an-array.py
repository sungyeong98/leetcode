class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        c=Counter()
        for idx,val in enumerate(nums):
            if val==key and idx+1<len(nums):
                c[nums[idx+1]]+=1
        return c.most_common(1)[0][0]