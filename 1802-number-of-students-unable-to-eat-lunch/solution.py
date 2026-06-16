class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        st,sa=deque(students),deque(sandwiches)

        someoneate=True
        curr=sa[0]
        while sa and someoneate:
            someoneate=False
            for _ in range(len(st)):
                stud=st.popleft()
                if stud==curr:
                    someoneate=True
                    sa.popleft()
                    if not sa:
                        return 0
                    curr=sa[0]
                else:
                    st.append(stud)

        return len(sa)
