class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        
        people.sort()

        boats = 0
        l,r = 0,len(people)-1

        while l<=r:
            total = people[l]+people[r]
            if total>limit:
                r-=1
            else:
                r-=1
                l+=1
            boats += 1
        
        return boats




