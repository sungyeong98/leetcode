class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ss,tt=Counter(s),Counter(t)
        temp=list(set(s+t))
        result=0

        for i in temp:
            if i not in ss:
                result+=tt[i]
            elif i not in tt:
                result+=ss[i]
            else:
                result+=abs(ss[i]-tt[i])
        return result