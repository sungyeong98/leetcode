class RecentCounter:

    def __init__(self):
        self.log=deque([])        

    def ping(self, t: int) -> int:
        if not self.log:
            self.log.append(t)
            return len(self.log)
        
        while self.log and self.log[0]<t-3000:
            self.log.popleft()
        self.log.append(t)
        return len(self.log)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)