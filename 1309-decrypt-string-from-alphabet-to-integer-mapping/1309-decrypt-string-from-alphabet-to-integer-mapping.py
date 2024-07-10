class Solution:
    def freqAlphabets(self, s: str) -> str:
        result,temp='',''
        flag=False

        for i in s[::-1]:
            if i=='#': 
                flag=True
                continue
            
            if flag and not temp:
                temp+=i
            elif flag and temp:
                temp=i+temp
                result+=chr(int(temp)+96)
                temp=''
                flag=False
            else:
                result+=chr(int(i)+96)
        return result[::-1]