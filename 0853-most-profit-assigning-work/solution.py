class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        jobs = sorted(zip(difficulty,profit))
        worker.sort()
        
        max_profit=0
        good_jobs = []
        for diff, prof in jobs:
            if good_jobs and prof <= good_jobs[-1][1]:
                continue
            good_jobs.append((diff, prof))

        res=0
        j=0
        for i in range(len(worker)):
            diff = worker[i]
            if good_jobs[j][0] > diff:
                continue
            
            while j+1<len(good_jobs) and not good_jobs[j+1][0] > diff:
                j+=1

            res+=good_jobs[j][1]
        return res
            
            
            



'''
sort by diff
sort
if there is a job that is harder but pays less we never want to do that job
'''
