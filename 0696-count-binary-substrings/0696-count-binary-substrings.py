class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        stack=[]
        temp=[]
        for i in s:
            if not stack:
                stack.append(i)
            else:
                if stack[-1]!=i:
                    temp.append(len(stack))
                    stack=[i]
                else:
                    stack.append(i)
        if stack:
            temp.append(len(stack))

        result=0
        for i in range(len(temp)-1):
            result+=min(temp[i],temp[i+1])
        return result