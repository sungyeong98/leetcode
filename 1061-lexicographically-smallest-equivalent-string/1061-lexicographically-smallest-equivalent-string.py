class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        word=[]
        for w1,w2 in zip(s1,s2):
            if not word:
                word.append(set({w1,w2}))
            else:
                for sub in word:
                    if w1 in sub or w2 in sub:
                        sub.add(w1)
                        sub.add(w2)
                        break
                else:
                    word.append(set({w1,w2}))
        result=''
        for i in baseStr:
            for sub in word:
                if i in sub:
                    result+=min(sub)
                    break
            else:
                result+=i
        return result