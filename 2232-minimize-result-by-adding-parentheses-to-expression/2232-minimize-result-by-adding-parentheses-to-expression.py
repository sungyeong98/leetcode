class Solution:
    def minimizeResult(self, expression: str) -> str:
        fix_ex=expression.split('+')
        result_num=sum(list(map(int,fix_ex)))
        result_ex=''
        for i in range(len(fix_ex[0])):
            for j in range(len(fix_ex[1])):
                left=fix_ex[0][:i]+'('+fix_ex[0][i:]
                right=fix_ex[1][:j+1]+')'+fix_ex[1][j+1:]

                new_ex=left+'+'+right

                left_num=int(fix_ex[0][:i]) if fix_ex[0][:i] else 1
                right_num=int(fix_ex[1][j+1:]) if fix_ex[1][j+1:] else 1
                middle_num=int(fix_ex[0][i:])+int(fix_ex[1][:j+1])

                new_num=middle_num*left_num*right_num

                if not result_ex:
                    result_ex=new_ex
                    result_num=new_num

                if new_num<result_num:
                    result_num=new_num
                    result_ex=new_ex
                
        return result_ex