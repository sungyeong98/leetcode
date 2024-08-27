class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        return sorted(c.keys(), key=lambda x:-c[x])[:k]
        