class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        prime=0
        for i in range(2,n+1):
            flag=True
            for j in range(2, int(math.sqrt(i)+1)):
                if i%j==0:
                    flag=False
                    break
            if flag:
                prime+=1
        num=n-prime
        return (math.factorial(prime)*math.factorial(num))%(10**9+7)
            