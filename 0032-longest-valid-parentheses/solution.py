class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:return 0

        st=[]
        st.append((-1,0))
        for i,ch in enumerate(s):
            if ch==")":
                if st and st[-1][1]=="(":
                    st.pop()
                    continue
            st.append((i,ch))
        st.append((len(s),0))
        # print(st)
        res=0
        for j in range(1,len(st)):
            i=j-1
            res=max(res,st[j][0]-st[i][0]-1)


        return res


