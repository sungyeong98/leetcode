class Solution:
    def divisorGame(self, n: int) -> bool:
        flag=True   #Alice turn
        while n>0:
            num=[i for i in range(1,n) if n%i==0]
            if not num:
                if flag:
                    return False
                else:
                    return True
            if flag:
                n-=num[0]
                flag=False
            else:
                n-=num[0]
                flag=True
        if flag:
            return False
        return True