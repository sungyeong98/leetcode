class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        code=97
        temp={}

        for i in key:
            if i==' ':  continue

            if i not in temp:
                temp[i]=chr(code)
                code+=1
        
        result=''
        for i in message:
            if i==' ':
                result+=' '
            else:
                result+=temp[i]
        return result