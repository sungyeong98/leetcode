class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        temp=[]
        for time in timePoints:
            split_time = time.split(':')
            total = int(split_time[0])*60 + int(split_time[1])
            temp.append(total)

        temp.sort()
        
        result = float('inf')
        for i in range(len(temp)-1):
            result=min(result, temp[i+1]-temp[i])

        result = min(result, 1440-temp[-1]+temp[0])
        return result