class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        i,j=0,0

        while i<len(v1) or j<len(v2):
            n1,n2=0,0
            while i<len(v1) and v1[i]!='.':
                n1=n1*10+int(v1[i])
                i+=1
            while j<len(v2) and v2[j]!='.':
                n2=n2*10+int(v2[j])
                j+=1
            if n1>n2:
                return 1
            if n1<n2:
                return -1
            i+=1
            j+=1
        
        return 0
