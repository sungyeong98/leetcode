class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        word_dict,words={},sentence.split(' ')
        for i in dictionary:
            word_dict[i]=len(i)
        
        result=[]
        for word in words:
            temp=word
            for original in word_dict:
                if word[:word_dict[original]]==original and \
                    len(word[:word_dict[original]])<len(temp):
                    temp=word[:word_dict[original]]
            result.append(temp)

        return ' '.join(result)