class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result=[]
        for i in range(left,right+1):
            flag=True
            for j in list(str(i)):
                if int(j)==0 or i%int(j)!=0:
                    flag=False
                    break
            if flag:
                result.append(i)
        return result