class Solution:
    def countTriples(self, n: int) -> int:
        result=0
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                temp=math.sqrt(i**2+j**2)
                if int(temp)==temp and int(temp)<=n:
                    result+=2
        return result