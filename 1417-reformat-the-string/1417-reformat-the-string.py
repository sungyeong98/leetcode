class Solution:
    def reformat(self, s: str) -> str:
        word,digit=[i for i in s if i.isalpha()],[i for i in s if i.isdigit()]
        if abs(len(word)-len(digit))>1:
            return ''
        if len(word)>len(digit):
            result=''
            for w,d in zip_longest(word,digit,fillvalue=None):
                if w is not None:
                    result+=w
                if d is not None:
                    result+=d
            return result
        
        else:
            result=''
            for d,w in zip_longest(digit,word, fillvalue=None):
                if d is not None:
                    result+=d
                if w is not None:
                    result+=w
            return result