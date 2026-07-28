class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits=[d for d in digits]
        digits.reverse()
        res=[]
        s=[(digits,[])]
        chars = {
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }
        while s:
            a,c=s.pop()
            if not a:
                res.append("".join(c))
            else:
                for ch in chars[int(a.pop())]:
                    s.append((a.copy(),c+[ch]))

        return res
