class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1,s2=[],[]
        for i,j in zip_longest(s,t,fillvalue=''):
            if i!='':
                if i.isalpha():
                    s1.append(i)
                else:
                    if s1:
                        s1.pop()
            if j!='':
                if j.isalpha():
                    s2.append(j)
                else:
                    if s2:
                        s2.pop()
        return True if s1==s2 else False