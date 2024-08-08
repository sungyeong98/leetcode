class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        result=[]
        m,n=len(box),len(box[0])

        step=0
        while step<m:
            for left in range(n-1):
                if box[step][left]=='*' or box[step][left]=='.':
                    continue
                for right in range(left+1,n):
                    if box[step][right]=='.':
                        box[step][left],box[step][right]=box[step][right],box[step][left]
                    elif box[step][right]=='*':
                        break
            step+=1

        for sub in list(zip(*box)):
            result.append(list(sub)[::-1])
        
        return result