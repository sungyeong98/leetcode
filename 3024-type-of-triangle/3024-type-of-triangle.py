class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        a,b,c=nums
        if (a+b<=c) or (a+c<=b) or (b+c<=a):
            return 'none'
        
        if a==b==c:
            return 'equilateral'
        elif a==b or a==c or b==c:
            return 'isosceles'
        else:
            return 'scalene'