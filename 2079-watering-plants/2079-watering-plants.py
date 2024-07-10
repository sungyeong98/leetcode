class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        result=0
        cap=capacity
        for i in range(len(plants)-1):
            result+=1
            cap-=plants[i]

            if cap<plants[i+1]:
                result+=2*(i+1)
                cap=capacity
        return result+1