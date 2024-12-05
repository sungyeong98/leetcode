class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        idx=0

        for i in range(1, len(intervals)):
            if intervals[idx][1] >= intervals[i][0]:
                intervals[idx][1] = max(intervals[idx][1], intervals[i][1])
            else:
                idx+=1
                intervals[idx]=intervals[i]
        return intervals[:idx+1]