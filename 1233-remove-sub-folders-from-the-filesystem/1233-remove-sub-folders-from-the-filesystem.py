class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()

        root=set()
        for i in folder:
            temp=i.split('/')
            for j in range(2,len(temp)+1):
                path='/'.join(temp[:j])
                if path in root:
                    break
            else:
                root.add(i)
        
        return root