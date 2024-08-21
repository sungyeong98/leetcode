class Solution:
    def arrangeWords(self, text: str) -> str:
        fixed_text=sorted([i.lower() for i in text.split(' ')], key=lambda x:len(x))
        fixed_text[0]=fixed_text[0][:1].upper()+fixed_text[0][1:]
        return ' '.join(fixed_text)