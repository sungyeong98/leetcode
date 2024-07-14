from collections import deque
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        element={}
        f=deque(list(formula))
        level=0
        while f:
            char=f.popleft()
            cnt=''
            if char.isupper():
                while f and f[0].islower():
                    char+=f.popleft()
            
                while f and f[0].isdigit():
                    cnt+=f.popleft()
                if not cnt:
                    cnt=1
                if char not in element:
                    element[char]={level:int(cnt)}
                else:
                    if level not in element[char]:
                        element[char][level]=int(cnt)
                    else:
                        element[char][level]+=int(cnt)
            elif char=='(':
                level+=1
            elif char==')':
                while f and f[0].isdigit():
                    cnt+=f.popleft()
                if not cnt:
                    cnt=1

                for ele in element:
                    if level in element[ele]:
                        element[ele][level]*=int(cnt)
                        for e in element[ele]:
                            if e<level:
                                element[ele][e]+=element[ele][level]
                            elif e==level:
                                if level-1 not in element[ele]:
                                    element[ele]={level-1:element[ele][level]}
                                
                level-=1

        result={}
        for ele in element:
            result[ele]=element[ele][min(element[ele])]
        
        result=sorted(result.items(), key=lambda x:(x[0],x[1]))

        answer=''
        for e,n in result:
            answer+=e
            if n>1:
                answer+=str(n)
        return answer