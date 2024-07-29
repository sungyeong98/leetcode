class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
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