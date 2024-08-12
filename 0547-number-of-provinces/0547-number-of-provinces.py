class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        city=defaultdict(list)

        for i in range(n):
            for j in range(n):
                if i!=j and isConnected[i][j]==1:
                    city[i].append(j)

        result=0
        not_visited_city=list(range(n))
        visited=set()
        while not_visited_city:
            city_num = not_visited_city.pop()
            if city_num not in city:
                result+=1
                continue
            if city_num in visited:
                continue

            stack=[city_num]
            visited.add(city_num)
            while stack:
                cur_city=stack.pop()

                for next_city in city[cur_city]:
                    if next_city in city and next_city not in visited:
                        visited.add(next_city)
                        stack.append(next_city)
            result+=1
        return result