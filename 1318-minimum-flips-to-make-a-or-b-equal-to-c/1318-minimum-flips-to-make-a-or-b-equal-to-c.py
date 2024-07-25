class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        aa=bin(a)[2:][::-1]
        bb=bin(b)[2:][::-1]
        cc=bin(c)[2:][::-1]
        result=0
        for n1,n2,n3 in zip_longest(aa,bb,cc,fillvalue='0'):
            if n3=='1':
                if n1=='0' and n2=='0':
                    result+=1
            else:
                if n1=='1' and n2=='1':
                    result+=2
                elif n1=='1' or n2=='1':
                    result+=1
        return result