class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        p=sorted(processorTime)
        f,s=[tasks[i]+p[1] for i in range(len(tasks)//2)],[tasks[i]+p[0] for i in range(len(tasks)//2,len(tasks))]

        return max(max(f),max(s))