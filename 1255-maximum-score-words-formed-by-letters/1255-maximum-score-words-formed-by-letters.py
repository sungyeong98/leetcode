from collections import Counter
from itertools import combinations
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        score_dict={chr(i+97):score[i] for i in range(len(score))}
        result=0

        pos_words=[]
        for word in words:
            wc=Counter(word)
            flag=True
            for w in wc:
                if w not in Counter(letters) or wc[w]>Counter(letters)[w]:
                    flag=False
                    break
            if flag:
                pos_words.append(word)


        for i in range(1,len(pos_words)+1):
            for j in combinations(pos_words,i):
                new_word=''.join(j)
                nwc=Counter(new_word)
                flag=True
                temp=0
                for w in nwc:
                    if nwc[w]>Counter(letters)[w]:
                        flag=False
                        break
                    temp+=(score_dict[w]*nwc[w])
                if flag:
                    if temp>result:
                        result=temp
        return result