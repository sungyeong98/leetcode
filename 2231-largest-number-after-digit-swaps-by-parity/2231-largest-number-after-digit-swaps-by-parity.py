class Solution:
    def largestInteger(self, num: int) -> int:
        n=list(str(num))
        even=sorted([i for i in n if int(i)%2==0],reverse=True)
        odd=sorted([i for i in n if int(i)%2==1],reverse=True)
        if int(n[0])%2==1:
            even,odd=odd,even
        result=''
        for e,o in zip_longest(even,odd,fillvalue=None):
            if e!=None:
                result+=e
            if o!=None:
                result+=o
        return int(result)