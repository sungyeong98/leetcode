class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        temp={}
        nums.sort()
        for i in range(1,len(nums)+1):
            t1,t2=deque(nums),deque(nums)
            min_num,max_num=0,0
            for _ in range(i):
                min_num+=t1.popleft()
                max_num+=t2.pop()
            for n in range(min_num,max_num+1):
                temp[n]=i

        result=[]
        for q in queries:
            if q in temp:
                result.append(temp[q])
            else:
                if q<min(temp.keys()):
                    result.append(0)
                elif q>max(temp.keys()):
                    result.append(len(nums))
        return result