class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        s=sentence.split(' ')
        vowel=['a', 'e', 'i', 'o', 'u']
        result=[]

        for idx,word in enumerate(s):
            temp=None
            if word[0].lower() in vowel:
                temp=word+'ma'
            else:
                if len(word)==1:
                    temp=word+'ma'
                else:
                    temp=word[1:]+word[0]+'ma'
            temp+='a'*(idx+1)
            result.append(temp)
        return ' '.join(result)