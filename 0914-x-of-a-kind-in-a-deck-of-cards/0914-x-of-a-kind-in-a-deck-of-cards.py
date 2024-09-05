class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        c=Counter(deck)
        temp=[i for i in c.values()]
        result=reduce(math.gcd,temp)
        return True if result>=2 else False