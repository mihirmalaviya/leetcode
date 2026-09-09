class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph=[[] for _ in range(n+1)]
        for u,v,w in times:
            heappush(graph[u],(v,w))
        pq=[(0,k)]

        dist=[float('inf')]*(n+1)
        dist[k]=0
        unseen=set([i+1 for i in range(n)])
        unseen.discard(k)

        while pq:
            currdist, curr = heappop(pq)

            if currdist>dist[curr]:
                continue
            
            for v,wt in graph[curr]:
                newdist=currdist+wt
                if newdist<dist[v]:
                    dist[v]=newdist
                    heappush(pq,(newdist,v))
                    unseen.discard(v)

        if not unseen:
            return max(dist[1:])

        return -1

