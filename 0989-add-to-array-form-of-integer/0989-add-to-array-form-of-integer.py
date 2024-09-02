class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n=int(''.join(list(map(str,num))))
        result=n+k
        return list(map(int,str(result)))