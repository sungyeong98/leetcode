class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        for i in range(ord('a'),ord('z')+1):
            word=word.replace(chr(i),' ')
        result=set([int(i) for i in word.split(' ') if i!=''])
        return len(result)