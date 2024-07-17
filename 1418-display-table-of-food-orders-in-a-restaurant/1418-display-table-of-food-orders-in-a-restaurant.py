class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        temp={}
        result=[]
        col_name=set()
        num_list=set()
        for _, table, menu in orders:
            if table not in temp:
                temp[table]=[menu]
            else:
                temp[table].append(menu)
            
            col_name.add(menu)
            num_list.add(int(table))
            
        col_name=list(sorted(col_name))
        num_list=list(sorted(num_list))

        result.append(['Table']+col_name)
        
        for num in num_list:
            row=[str(num)]
            for col in result[0][1:]:
                row.append(str(temp[str(num)].count(col)))
            result.append(row)
        
        return result