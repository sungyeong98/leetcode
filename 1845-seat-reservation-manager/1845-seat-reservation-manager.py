class SeatManager:

    def __init__(self, n: int):
        self.s=[i for i in range(1,n+1)]

    def reserve(self) -> int:
        return heapq.heappop(self.s)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.s, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)