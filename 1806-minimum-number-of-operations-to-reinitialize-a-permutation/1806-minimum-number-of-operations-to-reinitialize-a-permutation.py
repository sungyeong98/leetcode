class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm=[i for i in range(n)]
        temp=None

        result=0
        while temp!=perm:
            arr=[0 for _ in range(n)]
            if temp is None:
                temp=perm
            for i in range(n):
                if i%2==0:
                    arr[i]=temp[i//2]
                else:
                    arr[i]=temp[n//2+(i-1)//2]
            temp=arr
            result+=1
        return result