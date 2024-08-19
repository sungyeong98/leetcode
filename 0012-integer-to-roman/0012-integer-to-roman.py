class Solution:
    def intToRoman(self, num: int) -> str:
        num_dict={
            1:'I', 4:'IV',5:'V',9:'IX',
            10:'X',40:'XL',50:'L',90:'XC',
            100:'C',400:'CD',500:'D',900:'CM',
            1000:'M'
        }

        temp=[]
        while num>10:
            temp.append(num%10)
            num//=10
        temp.append(num)

        result=[]
        for idx, val in enumerate(temp):
            if int(str(val)+'0'*idx) in num_dict:
                fixed_str=int(str(val)+'0'*idx)
                result.append(num_dict[fixed_str])
            elif val>5:
                left,right=5,val-5
                left_str=int(str(left)+'0'*idx)
                right_str=int(str(1)+'0'*idx)
                fixed_str=num_dict[left_str]+num_dict[right_str]*right
                result.append(fixed_str)
            elif val<4:
                fixed_str=int(str(1)+'0'*idx)
                result.append(num_dict[fixed_str]*val)
        
        return ''.join(result[::-1])