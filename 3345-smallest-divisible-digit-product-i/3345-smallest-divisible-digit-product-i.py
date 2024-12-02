class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            str_num = str(n)
            temp = 1
            for i in str_num:
                temp*=int(i)
            if temp%t==0:
                return n
            n+=1