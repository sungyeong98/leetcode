class Solution:
    def numberToWords(self, num: int) -> str:
        num_pos_dict={3:'Billion', 2:'Million', 1:'Thousand'}
        num_dict={1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',
                10:'Ten',11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',
                16:'Sixteen',17:'Seventeen',18:'Eighteen',19:'Nineteen',
                20:'Twenty',30:'Thirty',40:'Forty',50:'Fifty',
                60:'Sixty',70:'Seventy',80:'Eighty',90:'Ninety'}

        #   숫자 분리
        def split_num(n):
            result=[]
            div=10**3
            while n>0:
                n,remainder=divmod(n,div)
                result.append(remainder)
            return result

        #   20미만의 숫자 변환
        def convert_19_under(n):
            return num_dict[n]

        #   20~99의 숫자 변환
        def convert_99_under(n):
            head,tail=divmod(n,10)
            result=num_dict[head*10]
            if not tail:
                return result
            else:
                return result+' '+num_dict[tail]

        #   100~999의 숫자 변환
        def convert_999_under(n):
            result=[]
            hundreds,remainder=divmod(n,100)
            if hundreds:
                result.append(num_dict[hundreds]+' Hundred')
            if remainder>=20:
                result.append(convert_99_under(remainder))
            elif remainder:
                result.append(convert_19_under(remainder))
            return ' '.join(result)

        def convert_num(n):
            if n==0:
                return 'Zero'

            result=[]
            num_list=split_num(n)

            for idx, val in enumerate(num_list):
                if word:=convert_999_under(val):
                    if idx:
                        word+=' '+num_pos_dict[idx]
                    result.append(word)
            return ' '.join(result[::-1])
        
        return convert_num(num)