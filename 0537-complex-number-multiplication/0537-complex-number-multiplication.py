class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        n1,n2=num1.split('+'),num2.split('+')
        real=int(n1[0])*int(n2[0])-(int(n1[1][:-1])*int(n2[1][:-1]))
        imaginary=int(n1[0])*int(n2[1][:-1])+int(n2[0])*int(n1[1][:-1])

        result=str(real)+'+'+str(imaginary)+'i'
        return result