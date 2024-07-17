class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result=''

        def gen(word,list):
            if len(word)==n:
                list.append(word)
                return list
            
            if word[-1]=='a':
                gen(word+'b',list)
                gen(word+'c',list)
            elif word[-1]=='b':
                gen(word+'a',list)
                gen(word+'c',list)
            else:
                gen(word+'a',list)
                gen(word+'b',list)
            
            if list:
                return list
        temp1,temp2,temp3=gen('a',[]),gen('b',[]),gen('c',[])
        temp=temp1+temp2+temp3
        temp.sort()
        if len(temp)<k:
            return result
        return temp[k-1]