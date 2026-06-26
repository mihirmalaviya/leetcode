class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            if nums[i]<=0 or nums[i]>len(nums):
                nums[i]=len(nums)+1

        for i in range(len(nums)):
            num=abs(nums[i])
            if num!=len(nums)+1:
                if nums[num-1]==abs(nums[num-1]):
                    nums[num-1]*=-1
        # print(nums)

        for i in range(len(nums)):
            if nums[i]==abs(nums[i]):
                return i+1
        return len(nums)+1
