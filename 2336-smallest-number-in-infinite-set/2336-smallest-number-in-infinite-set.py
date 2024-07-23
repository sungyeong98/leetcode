class SmallestInfiniteSet:

    def __init__(self):
        self.nums={i:True for i in range(1,1001)}

    def popSmallest(self) -> int:
        for n in self.nums:
            if self.nums[n]==True:
                self.nums[n]=False
                return n

    def addBack(self, num: int) -> None:
        self.nums[num]=True
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)