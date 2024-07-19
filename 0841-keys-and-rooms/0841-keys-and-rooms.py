class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=set()
        start=0
        stack=[start]
        visited.add(start)

        while stack:
            cur_key=stack.pop()

            for next_key in rooms[cur_key]:
                if next_key not in visited:
                    visited.add(next_key)
                    stack.append(next_key)
        
        if len(visited)!=len(rooms):
            return False
        return True