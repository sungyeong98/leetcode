class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        result=0
        prime_num=[2,3,5,7,11,13,17,19]
        for i in range(left,right+1):
            num=bin(i)[2:].count('1')
            if num in prime_num:
                result+=1
        return result