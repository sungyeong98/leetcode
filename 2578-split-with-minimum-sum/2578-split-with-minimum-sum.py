class Solution:
    def splitNum(self, num: int) -> int:
        temp=deque(sorted(list(map(int,str(num)))))
        n=len(temp)

        n1,n2='',''
        while temp:
            if temp:
                n1+=str(temp.popleft())
            if temp:
                n2+=str(temp.popleft())

        return int(n1)+int(n2)