class Solution:
    def minOperations(self, n: int) -> int:
        #solution1
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

        #solution2
        '''
        num = n//2 if n%2==0 else n//2+1

        target=(2*(num-1))+1 if n%2==1 else (2*(num-1))+2

        return sum([target-((2*i)+1) for i in range(num-1,-1,-1)])
        '''

        #solution3
        total=n*(n-1)+n
        mid=total//n

        n=mid//2
        if mid%2==1:
            return n*(n+1)
        return n*(n-1)+n