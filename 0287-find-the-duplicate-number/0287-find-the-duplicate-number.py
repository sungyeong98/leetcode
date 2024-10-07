class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
            counter = Counter(nums)
            for c in counter:
                if counter[c]>1:    return c