class Solution:
    def reformatNumber(self, number: str) -> str:
        pre_number=[i for i in number if i.isdigit()]
        result=''
        while pre_number:
            if len(pre_number)>4:
                result+=''.join(pre_number[:3])
                result+='-'
                pre_number=pre_number[3:]
            else:
                if len(pre_number)<4:
                    result+=''.join(pre_number)
                else:
                    result+=''.join(pre_number[:2])+'-'+''.join(pre_number[2:])
                break
        return result