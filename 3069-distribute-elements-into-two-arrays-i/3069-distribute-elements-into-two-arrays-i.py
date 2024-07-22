class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n=deque(nums)
        a1,a2=[n.popleft()],[n.popleft()]

        while n:
            if a1[-1]>a2[-1]:
                a1.append(n.popleft())
            else:
                a2.append(n.popleft())
        return a1+a2