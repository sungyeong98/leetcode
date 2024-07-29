class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        #solution1(6132ms   ->  효율성이 너무 떨어짐)
        '''
        cnt={i:0 for i in range(lo,hi+1)}
        num=[i for i in range(lo,hi+1)]
        visited=set()

        for i in num:
            if i not in visited:
                temp=[i]
                visited.add(i)
                n=i
                while n>1:
                    if n%2==0:
                        n//=2
                    else:
                        n=3*n+1
                    
                    for j in temp:
                        cnt[j]+=1

                    if n in num and n not in visited:
                        temp.append(n)
                        visited.add(n)

        result=sorted(cnt.keys(), key=lambda x:(cnt[x],x))
        return result[k-1]
        '''

        #solution2
        def power(n):
            if n in memo:
                return memo[n]

            cnt=0
            ori_n=n

            while n!=1:
                if n in memo:
                    cnt+=memo[n]
                    break
                if n%2==0:
                    n//=2
                else:
                    n=3*n+1
                cnt+=1
            memo[ori_n]=cnt
            return cnt
        memo={}
        result=[]
        for num in range(lo,hi+1):
            result.append((power(num),num))
        result.sort()
        return result[k-1][1]