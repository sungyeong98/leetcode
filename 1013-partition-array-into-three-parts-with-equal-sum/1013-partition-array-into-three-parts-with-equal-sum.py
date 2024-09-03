class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        s=sum(arr)
        if s%3!=0:
            return False
        c,a=0,0
        for i in range(len(arr)):
            c+=arr[i]
            if c==s//3:
                a+=1
                c=0
        return a==3