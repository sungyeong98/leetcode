class Solution:
    def beautySum(self, s: str) -> int:
        result=0
        n=len(s)

        #solution1
        '''
        for i in range(n-1):
            for j in range(i+1,n+1):
                counter=Counter(s[i:j])
                result+=(max(counter.values())-min(counter.values()))

        return result
        '''


        #solution2
        for i in range(n):
            temp=defaultdict(int)
            max_val=0

            for j in range(i,n):
                temp[s[j]]+=1

                max_val=max(max_val, temp[s[j]])
                min_val=min(temp.values())

                result+=(max_val-min_val)
        return result