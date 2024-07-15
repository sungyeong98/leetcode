class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n=len(pattern)
        num=[i for i in range(1,10)]

        for i in permutations(num,n+1):
            temp=list(i)
            flag=True
            for j in range(n):
                p=pattern[j]
                if p=='I' and temp[j]>temp[j+1]:
                    flag=False
                    break
                elif p=='D' and temp[j]<temp[j+1]:
                    flag=False
                    break
            if flag:
                return ''.join(list(map(str,temp)))