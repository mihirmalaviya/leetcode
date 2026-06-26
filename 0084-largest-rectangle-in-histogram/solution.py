class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        

        s=[]
        n=len(heights)
        res=0
        rightlower=[0]*n

        for i in range(n):
            h=heights[i]
            while s and heights[s[-1]]>h:
                j=s.pop()
                rightlower[j]=i-j
            s.append(i)
        
        stack=[]
        leftlower = [0]*n
        for i in reversed(range(n)):
            h=heights[i]
            while s and heights[s[-1]]>h:
                j=s.pop()
                leftlower[j]=j-i
            s.append(i)

        # print(rightlower)
        # print(leftlower)

        for i in range(n):
            h=heights[i]
            r=rightlower[i]
            if r==0:
                r=n-i
            l=leftlower[i]
            if l==0:
                l=i+1
            res=max(res,(l+r-1)*h)

        return res


