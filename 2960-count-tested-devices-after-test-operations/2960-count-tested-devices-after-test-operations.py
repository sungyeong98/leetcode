class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        result=0
        n=len(batteryPercentages)

        for i in range(n):
            if batteryPercentages[i]>0:
                for j in range(i+1,n):
                    batteryPercentages[j]-=1
                    if batteryPercentages[j]<0:
                        batteryPercentages[j]=0
                result+=1
        return result