class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph=defaultdict(list)
        level=[0]*(n+1)

        for prev, next in relations:
            graph[prev].append(next)
            level[next]+=1
        
        q=deque()
        min_time=[0]*(n+1)

        for i in range(1,n+1):
            if level[i]==0:
                q.append(i)
                min_time[i]=time[i-1]
        
        while q:
            course=q.popleft()
            for next_course in graph[course]:
                level[next_course]-=1
                min_time[next_course]=max(min_time[next_course], min_time[course] + time[next_course-1])

                if level[next_course]==0:
                    q.append(next_course)

        return max(min_time)