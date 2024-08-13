class FreqStack:

    def __init__(self):
        self.count=defaultdict(int)
        self.max_heap=[]
        self.level=0

    def push(self, val: int) -> None:
        self.count[val]+=1
        self.level+=1
        heapq.heappush(self.max_heap,(-self.count[val], -self.level, val))

    def pop(self) -> int:
        num=heapq.heappop(self.max_heap)[2]
        self.count[num]-=1
        return num
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()