class Solution:
    def isFascinating(self, n: int) -> bool:
        c=Counter()
        for i in range(1,4):
            temp=str(n*i)
            for num in temp:
                if int(num)==0:
                    return False
                c[int(num)]+=1
                if c[int(num)]>1:
                    return False
        return True