class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        num, flag = 1, True
        cnt=0

        while cnt<time:
            if flag==True:
                if num<n:
                    num+=1
                else:
                    flag=False
                    num-=1
            else:
                if num>1:
                    num-=1
                else:
                    flag=True
                    num+=1
            cnt+=1
        
        return num