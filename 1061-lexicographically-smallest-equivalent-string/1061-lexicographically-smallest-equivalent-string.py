class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        s=set(s1+s2+baseStr)
        temp={i:float('inf') for i in s}
        level=1

        for w1,w2 in zip(s1,s2):
            if temp[w1]!=float('inf') or temp[w2]!=float('inf'):
                min_level=min(temp[w1],temp[w2])
                temp[w1]=min_level
                temp[w2]=min_level
            else:
                temp[w1]=level
                temp[w2]=level
                level+=1
        
        for _ in range(len(s)):
            for w1,w2 in zip(s1,s2):
                min_level=min(temp[w1],temp[w2])
                temp[w1]=min_level
                temp[w2]=min_level
        
        level_dict={}
        for w in temp:
            l=temp[w]
            if l!=float('inf'):
                if l not in level_dict:
                    level_dict[l]=w
                else:
                    level_dict[l]=min(level_dict[l],w)
        
        result=''
        for w in baseStr:
            if temp[w]==float('inf'):
                result+=w
            else:
                result+=level_dict[temp[w]]
        return result