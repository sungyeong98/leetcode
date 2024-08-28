class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        start=s[0]
        idx=goal.index(start)
        return True if s==goal[idx:]+goal[:idx] else False