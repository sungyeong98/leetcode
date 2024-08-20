class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result=[]
        m,n=len(str(low)),len(str(high))
        num=list(range(1,10))
        for i in range(m,n+1):
            for j in range(len(num)-i+1):
                temp=int(''.join(list(map(str,num[j:j+i]))))
                if low<=temp<=high:
                    result.append(temp)
        result.sort()
        return result