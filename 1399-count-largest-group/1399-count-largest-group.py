class Solution:
    def countLargestGroup(self, n: int) -> int:
        temp=defaultdict(int)
        for i in range(1,n+1):
            str_num=list(str(i))
            sum_num=sum(list(map(int,str_num)))
            temp[sum_num]+=1
        result=sum([1 for i in temp.keys() if temp[i]==max(temp.values())])
        return result