class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        
        people.sort()
        people.reverse()
        l=0
        r=len(people)-1
        res=0
        while l<=r:
            cap=limit
            cap-=people[l]
            l+=1
            if people[r]<=cap:
                r-=1
            res+=1
        return res

