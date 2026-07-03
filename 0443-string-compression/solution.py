class Solution:
    def compress(self, chars: List[str]) -> int:
        l=0
        chars.append("\0")

        count=1
        curr=chars[0]
        r=1
        while r<len(chars):
            ch=chars[r]
            if ch==curr:
                count+=1
            else:
                chars[l]=curr
                l+=1
                if count>1:
                    s=str(count)
                    for num in s:
                        chars[l]=num
                        l+=1
                count=1
                curr=ch
            r+=1
        

        return l

            


