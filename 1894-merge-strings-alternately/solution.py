class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        res=[]
        a,b=0,0
        while a<len(word1) and b<len(word2):
            res.append(word1[a])
            res.append(word2[b])
            a+=1
            b+=1
        while a<len(word1):
            res.append(word1[a])
            a+=1
        while b<len(word2):
            res.append(word2[b])
            b+=1
        return "".join(res)

        
