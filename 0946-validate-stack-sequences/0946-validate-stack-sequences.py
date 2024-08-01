class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pu=deque(pushed)
        po=deque(popped)
        stack=[]
        while pu:
            stack.append(pu.popleft())
            while stack and stack[-1]==po[0]:
                stack.pop()
                po.popleft()
        return True if not stack else False