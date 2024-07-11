class Solution:
    def countVowelStrings(self, n: int) -> int:
        num=n+5-1
        return reduce(lambda x,y:x*y,list(range(num,num-n,-1)))//reduce(lambda x,y:x*y,list(range(n,0,-1)))