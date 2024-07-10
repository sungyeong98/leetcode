class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n=len(s)
        temp={s[i]:i for i in range(n)}

        idx, result=0,[]
        while idx<n:
            end, j=temp[s[idx]],idx+1
            while j<end:
                if temp[s[j]]>end:
                    end=temp[s[j]]
                j+=1
            result.append(end-idx+1)
            idx=end+1
        return result