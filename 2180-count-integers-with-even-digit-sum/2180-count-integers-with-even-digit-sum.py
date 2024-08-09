class Solution:
    def countEven(self, num: int) -> int:
        result=0
        for i in range(2,num+1):
            str_num=str(i)
            if sum(list(map(int,list(str_num))))%2==0:
                result+=1
        return result