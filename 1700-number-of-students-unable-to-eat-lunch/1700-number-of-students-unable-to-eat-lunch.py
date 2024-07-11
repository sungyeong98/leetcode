class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        st,sa=deque(students),deque(sandwiches)
        while len(st)>0 and sa[0] in st:
            if sa[0]==st[0]:
                st.popleft()
                sa.popleft()
            else:
                st.append(st.popleft())
        return len(st)