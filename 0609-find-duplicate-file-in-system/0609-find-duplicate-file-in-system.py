class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        file_dict={}
        for p in paths:
            temp=p.split(' ')
            path=temp[0]

            for file in temp[1:]:
                left,right=file.index('('),file.index(')')
                content=file[left:right+1]
                file_name=file[:left]

                if content not in file_dict:
                    file_dict[content]=[path+'/'+file_name]
                else:
                    file_dict[content].append(path+'/'+file_name)

        result=[]
        for c in file_dict:
            if len(file_dict[c])>1:
                result.append(file_dict[c])
        return result