class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        temp=[1,1]

        while k>temp[-1]:
            temp.append(temp[-1]+temp[-2])

        result=0
        while k>0:
            if k<temp[-1]:
                temp.pop()
            elif k not in temp and k>=temp[-1]:
                k-=temp[-1]
                result+=1
                temp.pop()
            elif k in temp:
                result+=1
                break
        return result