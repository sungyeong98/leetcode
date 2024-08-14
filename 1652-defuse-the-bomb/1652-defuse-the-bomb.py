class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k==0:    return [0]*len(code)

        n=len(code)
        result=[]
        if k>0:
            for i in range(n):
                temp=0
                idx=(i+1)%n
                cnt=0
                while cnt<k:
                    temp+=code[idx]
                    idx=(idx+1)%n
                    cnt+=1
                result.append(temp)
        else:
            code.reverse()
            for i in range(n-1,-1,-1):
                temp=0
                idx=(i+1)%n
                cnt=0
                while cnt<abs(k):
                    temp+=code[idx]
                    idx=(idx+1)%n
                    cnt+=1
                result.append(temp)
        
        return result