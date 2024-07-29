class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        def generate(bit):
            if bit==0:
                return ['']
            small=generate(bit-1)
            result=[]

            for code in small:
                result.append('0'+code)
            
            for code in reversed(small):
                result.append('1'+code)
            
            return result

        gray_code=deque(generate(n))

        while int(gray_code[0],2)!=start:
            gray_code.append(gray_code.popleft())
        
        return [int(i,2) for i in gray_code]