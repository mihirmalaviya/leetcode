class Solution:
    def simplifyPath(self, path: str) -> str:

        path=(path.split('/'))
        s=[]
        for x in path:
            if not x:
                continue

            if x=="..":
                if s:
                    s.pop()
            elif x==".":
                pass
            else:
                s.append(x)
        
        return "/"+"/".join(s)

        
