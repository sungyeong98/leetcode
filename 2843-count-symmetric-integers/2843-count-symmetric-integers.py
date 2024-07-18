class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result=0
        for num in range(low,high+1):
            temp=str(num)
            if len(temp)%2==0:
                left,right=temp[:len(temp)//2],temp[len(temp)//2:]
                if sum(list(map(int,list(left))))==sum(list(map(int,list(right)))):
                    result+=1
        return result