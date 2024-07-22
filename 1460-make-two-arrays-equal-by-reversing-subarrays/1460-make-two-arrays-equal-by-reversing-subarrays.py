class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        t,a=Counter(target),Counter(arr)
        temp=list(set(target+arr))
        for i in temp:
            if t[i]!=a[i]:
                return False
        return True