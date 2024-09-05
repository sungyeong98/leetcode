class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:  return False

        n=len(arr)
        left,right,lenght=0,-1,n

        while left<lenght-1 and arr[left]<arr[left+1]:
            left+=1
        while right>-lenght and arr[right]<arr[right-1]:
            right-=1
        
        return left==right+lenght and 0<left and right<-1