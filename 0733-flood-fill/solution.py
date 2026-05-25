class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        m,n = len(image), len(image[0])
        friend_color = image[sr][sc]

        if color == friend_color: 
            return image

        stack = [(sr,sc)]
        while stack:
            y, x = stack.pop()
            if image[y][x] == friend_color:
                image[y][x] = color 
                # add adjacent to stack for processing
                if y-1>=0: stack.append((y-1,x))
                if x-1>=0: stack.append((y,x-1))
                if y+1<m: stack.append((y+1,x))
                if x+1<n: stack.append((y,x+1))

        return image
        
        
