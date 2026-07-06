class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        q=deque()
        for y in range(len(mat)):
            for x in range(len(mat[0])):
                if mat[y][x]==0:
                    q.append((y,x))
                else:
                    mat[y][x]=-1
        
        i=0
        while q:
            for _ in range(len(q)):
                y,x=q.popleft()
                if y-1>=0 and mat[y-1][x]==-1:
                    q.append((y-1,x))
                if y+1<len(mat) and mat[y+1][x]==-1:
                    q.append((y+1,x))
                if x-1>=0 and mat[y][x-1]==-1:
                    q.append((y,x-1))
                if x+1<len(mat[0]) and mat[y][x+1]==-1:
                    q.append((y,x+1))
                if mat[y][x]==-1:
                    mat[y][x]=i
            i+=1

        return mat

'''
add them all to q

while q:
    for _ in q:
        q.popleft
        add all the ones that are next to it if they havent been seen yet
        update each part of the thing to be thing
'''
