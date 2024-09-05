class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        c=Counter(deck)
        temp=[i for i in c.values() if i>1]
        return True if len(set(temp))==1 else False