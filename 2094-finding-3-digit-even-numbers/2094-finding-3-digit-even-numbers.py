class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count=[0]*10
        for i in digits:
            count[i]+=1

        result=[]
        for i in range(0,10,2):
            if count[i]==0:
                continue
            count[i]-=1

            for j in range(10):
                if count[j]==0:
                    continue
                count[j]-=1

                for k in range(1,10):
                    if count[k]>=1:
                        result.append(100*k+10*j+i)
                count[j]+=1
            count[i]+=1
        return sorted(result)