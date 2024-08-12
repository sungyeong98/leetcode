from sortedcontainers import SortedList
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.num_list=SortedList(nums, key=lambda x:-x)

    def add(self, val: int) -> int:
        self.num_list.add(val)
        return self.num_list[self.k-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)