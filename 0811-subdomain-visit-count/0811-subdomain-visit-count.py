class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        temp={}
        for domain in cpdomains:
            num,d=domain.split(' ')
            num=int(num)

            sub_d=d.split('.')
            for i in range(len(sub_d)):
                if '.'.join(sub_d[i:]) not in temp:
                    temp['.'.join(sub_d[i:])]=num
                else:
                    temp['.'.join(sub_d[i:])]+=num

        result=[]
        for i in temp:
            result.append(str(temp[i])+' '+i)
        return result