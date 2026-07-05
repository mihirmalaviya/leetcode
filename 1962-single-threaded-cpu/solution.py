class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([(x[0],x[1],i) for i,x in enumerate(tasks)])
        i=0
        time=tasks[0][0]
        heap=[]
        res=[]
        while len(res)<len(tasks):
            while i<len(tasks) and tasks[i][0]<=time:
                heappush(heap, (tasks[i][1],tasks[i][2]))
                i+=1

            if heap:
                p,idx = heappop(heap)
                res.append(idx)
                time+=p
            elif i<len(tasks):
                time=tasks[i][0]
        return res

'''
first sort it

keep track of time, and initialize time as the enque time of the first task

then keep adding as time allows
pop
update time

'''
