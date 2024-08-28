class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        str_num=str(num)
        n=len(str_num)
        result=0
        for i in range(n-k+1):
            temp=int(str_num[i:i+k])
            if temp!=0 and num%temp==0:
                result+=1
        return result