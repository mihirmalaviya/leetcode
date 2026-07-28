class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = list(zip(position,speed))
        cars.sort()
        cars.reverse()

        s=[]
        for p,v in cars:
            time=(target-p)/v
            if not s or time > s[-1]:
                # print(p,v)
                s.append(time)

        return len(s)

'''



'''
