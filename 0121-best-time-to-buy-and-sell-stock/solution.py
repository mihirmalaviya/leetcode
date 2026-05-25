class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        curr_min = prices[0]
        max_profit = 0
        for price in prices[1:]:
            if price<curr_min:
                curr_min = price
            else:
                max_profit = max(max_profit, price-curr_min)

        return max_profit


"""
7,1,5,3,6,4
  ^ ^
first min
first max

"""
