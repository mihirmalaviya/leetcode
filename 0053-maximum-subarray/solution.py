class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # best_sum = float('-inf')
        # curr_sum = 0
        # l,r=0,0
        # while r<len(nums):
        #     curr_sum += nums[r]
        #     r+=1

        #     best_sum = max(best_sum,curr_sum)

        #     if r!=len(nums) and curr_sum < 0: 
        #         while l<r:
        #             curr_sum -= nums[l]
        #             l+=1
                
        # best_sum = max(best_sum,curr_sum)

        # return best_sum

        # Kadanes algo
        curr_max, max_till_now = 0, float('-inf')
        for n in nums:
            curr_max = max(n, curr_max+n)
            max_till_now = max(curr_max, max_till_now)
            
        return max_till_now
