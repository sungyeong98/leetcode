class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        start=s[0]
        idx=[i for i,w in enumerate(goal) if w==start]
        for i in idx:
            if goal[i:]+goal[:i]==s:
                return True
        return False