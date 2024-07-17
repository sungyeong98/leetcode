class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        temp=defaultdict(list)
        for i,j in adjacentPairs:
            temp[i].append(j)
            temp[j].append(i)

        start=None
        for key,val in temp.items():
            if len(val)==1:
                start=key
                break
        
        result, current, prev = [], start, None
        while current is not None:
            result.append(current)
            next_nodes=temp[current]

            next_node=next_nodes[0] if next_nodes[0]!=prev else (next_nodes[1] if len(next_nodes)>1 else None)

            prev=current
            current=next_node
        
        return result