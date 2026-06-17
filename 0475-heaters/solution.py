class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()

        res=0
        i=0
        for house in houses:
            while i+1<len(heaters) and heaters[i]<house:
                i+=1
            
            if heaters[i]<house:
                res=max(res,abs(heaters[i]-house))
            else:
                mindist=abs(heaters[i]-house)
                if i>0:
                    mindist=min(mindist, abs(heaters[i-1]-house))
                res=max(res,mindist)
            
        return res
                
'''

sort both

2 pointers

each house is either between 2 heaters or behind 1 or past last one

for each house
while heater1 isnt <= house and heater2 isnt >= house
increment

update max min dist

return

'''
        
