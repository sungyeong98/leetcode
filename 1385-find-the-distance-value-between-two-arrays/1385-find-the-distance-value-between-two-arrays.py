class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        result=0
        for i in arr1:
            flag=False
            for j in arr2:
                if abs(i-j)<=d:
                    flag=True
                    break
            if not flag:
                result+=1
        return result