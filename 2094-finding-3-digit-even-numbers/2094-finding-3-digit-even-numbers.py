class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result=set()
        n=len(digits)
        for i in range(n):
            if digits[i]!=0:
                for j in range(n):
                    for k in range(n):
                        if i!=j and i!=k and j!=k and digits[k]%2==0:
                            temp=int(str(digits[i])+str(digits[j])+str(digits[k]))
                            result.add(temp)
        return sorted(result)