class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        target=deque(list(range(left,right+1)))
        for s,e in ranges:
            while target and s<=target[0]<=e:
                target.popleft()
        return True if not target else False