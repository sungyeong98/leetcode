class Solution:
    def minOperations(self, n: int) -> int:
        '''
        num=n//2
        if n%2==1:  num+=1
        temp=[(2*i)+1 for i in range(num-1,-1,-1)]
        target=temp[0] if n%2==1 else temp[0]+1

        result=0
        for i in temp:
            result+=target-i
        return result
        '''

        num = n//2 if n%2==0 else n//2+1

        target=(2*(num-1))+1 if n%2==1 else (2*(num-1))+2

        return sum([target-((2*i)+1) for i in range(num-1,-1,-1)])