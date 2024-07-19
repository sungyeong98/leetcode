class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys=[i for i in range(len(rooms))]
        temp=[0]
        for i in range(len(rooms)):
            for j in rooms[i]:
                if i!=j:
                    temp.append(j)
        
        if len(set(keys)&set(temp))!=len(keys):
            return False
        return True