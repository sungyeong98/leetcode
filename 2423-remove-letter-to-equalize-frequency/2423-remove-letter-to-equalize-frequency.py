class Solution:
    def equalFrequency(self, word: str) -> bool:
        c=Counter(Counter(word).values())
        if len(c)==1:
            return list(c.keys())[0]==1 or list(c.values())[0]==1
        if len(c)==2:
            temp1,temp2=min(c.keys()),max(c.keys())
            return (temp1+1==temp2 and c[temp2]==1) or (temp1==1 and c[temp1]==1)
        return False