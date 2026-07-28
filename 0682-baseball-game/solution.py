class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        
        s=[]
        for o in operations:
            if o=="C":
                s.pop()
            elif o=="D":
                s.append(2*s[-1])
            elif o=="+":
                s.append(s[-2]+s[-1])
            else:
                s.append(int(o))
        return sum(s)
