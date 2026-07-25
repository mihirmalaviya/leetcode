class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        delrow=False
        delcol=False
        
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x]==0:
                    matrix[0][x]='a'
                    matrix[y][0]='a'
                    if x==0:
                        delcol=True
                    if y==0:
                        delrow=True
        
        for y in reversed(range(1,len(matrix))):
            for x in reversed(range(1,len(matrix[0]))):
                if matrix[0][x]=='a' or matrix[y][0]=='a':
                    matrix[y][x]=0

        
        for i in range(len(matrix)):
            if delcol:
                matrix[i][0]=0
            else:
                if matrix[i][0]=='a':
                    matrix[i][0]=0
        
        for i in range(len(matrix[0])):
            if delrow:
                matrix[0][i]=0
            else:
                if matrix[0][i]=='a':
                    matrix[0][i]=0
