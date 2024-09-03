class Solution:
    def reorderSpaces(self, text: str) -> str:
        if len(text)==1:    return text
        cnt=text.count(' ')
        words=[i for i in text.split(' ') if i!='']

        use_cnt=cnt//(len(words)-1) if len(words)>1 else 0
        re_cnt=cnt%(len(words)-1) if len(words)>1 else cnt

        result=(' '*use_cnt).join(words)+' '*re_cnt
        return result