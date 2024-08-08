class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        if len(set(s))<3:
            return 0
        word_idx=defaultdict(list)
        n=len(s)
        result=0

        for idx,w in enumerate(s):
            word_idx[w].append(idx)

        for word in word_idx:
            for idx in word_idx[word]:
                a_list=[i for i in word_idx['a'] if i>idx]
                b_list=[i for i in word_idx['b'] if i>idx]
                c_list=[i for i in word_idx['c'] if i>idx]

                if word=='a':
                    if b_list and c_list:
                        temp=max(min(b_list),min(c_list))
                        result+=n-temp
                elif word=='b':
                    if a_list and c_list:
                        temp=max(min(a_list),min(c_list))
                        result+=n-temp
                else:
                    if a_list and b_list:
                        temp=max(min(a_list),min(b_list))
                        result+=n-temp
        return result