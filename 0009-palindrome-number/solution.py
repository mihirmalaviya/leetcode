class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x!=abs(x): return False
        nums=[]
        while x:
            r=x%10
            x//=10
            nums.append(r)
        # print(nums)

        return nums == nums[::-1]
        


