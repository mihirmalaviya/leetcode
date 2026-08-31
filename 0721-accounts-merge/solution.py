class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        parents=list(range(len(accounts)))

        def find(x):
            if x!=parents[x]:
                parents[x]=find(parents[x])
            return parents[x]

        def union(x,y):
            parents[find(x)]=find(y)
        
        owner={} # email -> owner
        for i,(_,*emails) in enumerate(accounts):
            for email in emails:
                if email in owner:
                    union(i,owner[email])
                owner[email]=i
        
        res=defaultdict(list)
        for email, i in owner.items():
            res[find(i)].append(email)

        return [[accounts[i][0]] + sorted(emails) for i,emails in res.items()]


