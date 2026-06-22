class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        i=0
        n=len(words)
        lines=[]
        line=[]
        count=0
        while i<n:
            word=words[i]
            if count+len(word)+len(line)<=maxWidth:
                line.append(word)
                count+=len(word)
            else:
                # print(line)
                space_budget=maxWidth-count
                if len(line)>1:
                    spaces=len(line)-1
                    minspace=(space_budget//spaces)
                    extras=(space_budget-spaces*(space_budget//spaces))
                    sofar=""
                    for j in range(len(line)-1):
                        w=line[j]
                        if extras>0:
                            sofar=sofar+w+" "*(minspace+1)
                            extras-=1
                        else:
                            sofar=sofar+w+" "*minspace
                    lines.append(sofar+line[-1])
                else:
                    lines.append(line[0]+' '*space_budget)

                line=[]
                count=0
                i-=1
            i+=1
            
        if line:
            if len(line)>1:
                space_budget=maxWidth-count-(len(line)-1)
                lines.append(' '.join(line)+' '*space_budget)
            else:
                space_budget=maxWidth-count
                lines.append(' '.join(line)+' '*space_budget)

        return lines


 
        
'''
for each word

keep adding len word if possible while keeping count+len(line)-1<=maxWidth

then justify it by getting the number of spaces (len(line)-1) and then taking teh remaining spaces (maxWidth-count+1) and then returning that //

if its a single word then left justify and if its the end left justify

'''
