from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        tt, ss = Counter(t), Counter(s)
        result=0
        for i in tt:
            if i not in ss:     result+=tt[i]
            else:       result+=abs(tt[i]-ss[i])
        for i in ss:
            if i not in tt:     result+=ss[i]
        return result//2