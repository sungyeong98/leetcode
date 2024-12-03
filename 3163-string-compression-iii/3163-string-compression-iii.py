class Solution:
    def compressedString(self, word: str) -> str:
        result, temp = '', ''
        idx=0
        while idx<len(word):
            if not temp or temp[-1]==word[idx]:
                temp+=word[idx]
                if len(temp)==9:
                    result+=str(9)+temp[-1]
                    temp=''
            else:
                result+=str(len(temp))+temp[-1]
                temp=''
                temp+=word[idx]
            idx+=1
        if temp:
            result+=str(len(temp))+temp[-1]
        return result