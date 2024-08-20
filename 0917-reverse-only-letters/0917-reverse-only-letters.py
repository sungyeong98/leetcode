class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        fixed_word=[i for i in s if i.isalpha()]
        rev=iter(fixed_word[::-1])
        result=''
        for i in s:
            if not i.isalpha():
                result+=i
            else:
                result+=next(rev)
        return result