class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        t_dict=defaultdict(list)

        for i in range(len(t)):
            for j in range(i+1,len(t)+1):
                temp=t[i:j]
                length=len(temp)
                if length<=len(s):
                    t_dict[length].append(temp)

        result=0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                temp=s[i:j]
                n=len(temp)

                for c in t_dict[n]:
                    cnt=sum([1 for a,b in zip(temp,c) if a!=b])
                    if cnt==1:
                        result+=1
        return result