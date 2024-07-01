class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        pos=[]
        n=len(boxes)
        for i in range(n):
            if boxes[i]=='1':
                pos.append(i)
        result=[]
        for i in range(n):
            cnt=0
            for j in pos:
                cnt+=abs(i-j)
            result.append(cnt)
        return result