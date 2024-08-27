class Solution:

    def __init__(self, nums: List[int]):
        self.idx=defaultdict(list)
        for idx,num in enumerate(nums):
            self.idx[num].append(idx)

    def pick(self, target: int) -> int:
        return random.choice(self.idx[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)