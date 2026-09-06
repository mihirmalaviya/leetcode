class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def next(x):
            return (x+nums[x]) % n
        
        n=len(nums)
        for i in range(n):
            f,s=next(i),i
            while nums[s] * nums[f]>0 and nums[s] * nums[next(f)]>0:
                if s==f:
                    if s==next(s):
                        break
                    return True
                s=next(s)
                f=next(next(f))
            s=i
            while nums[s]*nums[next(s)]>0:
                temp=s
                s=next(s)
                nums[temp]=0

        return False


