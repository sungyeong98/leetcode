class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        temp=[idx+1 if word[:len(searchWord)]==searchWord else float('inf') for idx,word in enumerate(sentence.split(' '))]
        result=[i for i in temp if i!=float('inf')]
        return result[0] if result else -1