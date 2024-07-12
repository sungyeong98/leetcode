class Solution:
    def sumBase(self, n: int, k: int) -> int:
        if k==10:
            return sum([int(i) for i in list(str(n))])
        
        temp=[]
        while n>k:
            temp.append(n//k)
            n%=k
        temp.append(n)
        return sum(temp)