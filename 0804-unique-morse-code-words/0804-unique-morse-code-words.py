class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        result=set()
        code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
            temp=''
            for w in word:
                temp+=code[ord(w)-ord('a')]
            result.add(temp)
        return len(list(result))