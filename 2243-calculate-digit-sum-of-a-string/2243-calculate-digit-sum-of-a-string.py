class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            n=len(s)
            temp=[]
            for i in range(0,n,k):
                sum_num=sum(list(map(int,s[i:i+k])))
                temp.append(str(sum_num))
            s=''.join(temp)
        return s