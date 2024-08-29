class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        x_dict, y_dict = defaultdict(list), defaultdict(list)
        p={(i,j) for i,j in stones}

        for i,j in stones:
            x_dict[i].append(j)
            y_dict[j].append(i)

        def remove(x,y):
            p.discard((x,y))
            for j in x_dict[x]:
                if (x,j) in p:
                    remove(x,j)
            for i in y_dict[y]:
                if (i,y) in p:
                    remove(i,y)

        result=0
        for i,j in stones:
            if (i,j) in p:
                remove(i,j)
                result+=1
        
        return len(stones)-result