class MyCalendarThree:

    def __init__(self):
        self.log=defaultdict(int)

    def book(self, startTime: int, endTime: int) -> int:
        self.log[startTime]+=1
        self.log[endTime]-=1

        max_k, event = 0, 0
        for t in sorted(self.log):
            event+=self.log[t]
            if event>max_k:
                max_k=event
        return max_k


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)