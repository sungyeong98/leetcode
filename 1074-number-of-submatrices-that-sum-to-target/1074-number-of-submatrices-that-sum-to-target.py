class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m,n=len(matrix),len(matrix[0])
        result=0

        for row_start in range(m):
            prefix_sum=[0]*n
            for row_end in range(row_start,m):
                for col in range(n):
                    prefix_sum[col]+=matrix[row_end][col]
            
                prefix_sum_count=defaultdict(int)
                prefix_sum_count[0]=1

                cur_sum=0
                for col in range(n):
                    cur_sum+=prefix_sum[col]
                    if cur_sum-target in prefix_sum_count:
                        result+=prefix_sum_count[cur_sum-target]
                    
                    prefix_sum_count[cur_sum]+=1
        return result