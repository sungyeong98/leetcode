from sortedcontainers import SortedList
class SORTracker:

    def __init__(self):
        self.locations=SortedList()
        self.cnt=0

    def add(self, name: str, score: int) -> None:
        self.locations.add((-score,name))

    def get(self) -> str:
        location=self.locations[self.cnt][1]
        self.cnt+=1
        return location
        


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()