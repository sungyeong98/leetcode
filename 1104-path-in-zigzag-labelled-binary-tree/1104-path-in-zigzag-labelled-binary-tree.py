class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        level=int(log(label,2))
        result=deque()
        for i in range(level, -1, -1):
            result.appendleft(label)
            label=(3*(2**i)-1-label)//2
        return result