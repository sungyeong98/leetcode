class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        words=[]
        for i in s:
            temp=[]
            if not words:
                if i.isalpha():
                    temp.append(i.lower())
                    temp.append(i.upper())
                else:
                    temp.append(i)
            else:
                for w in words[-1]:
                    if i.isalpha():
                        temp.append(w+i.lower())
                        temp.append(w+i.upper())
                    else:
                        temp.append(w+i)
            words.append(temp)
        return words[-1]