class Solution:
    def minOperations(self, n: int) -> int:
        num=n//2
        if n%2==1:  num+=1
        temp=[(2*i)+1 for i in range(num-1,-1,-1)]
        target=temp[0] if n%2==1 else temp[0]+1

        result=0
        for i in temp:
            result+=target-i
        return result