class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        users={}
        for user,time in logs:
            if user not in users:
                users[user]=set()
                users[user].add(time)
            else:
                users[user].add(time)

        result=[0]*k

        for i in users:
            n=len(users[i])
            result[n-1]+=1
        return result