class Solution:
    def largestInteger(self, num: int) -> int:
        n=list(str(num))
        even=iter(sorted([i for i in n if int(i)%2==0],reverse=True))
        odd=iter(sorted([i for i in n if int(i)%2==1],reverse=True))
        result=''
        for i in n:
            if int(i)%2==0:
                result+=next(even)
            else:
                result+=next(odd)
        return int(result)