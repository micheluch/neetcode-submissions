class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_index = 0
        for i in range(0, len(prices)):
            profit = prices[i] - prices[min_index]
            max_profit = profit if profit > max_profit else max_profit
            if prices[i] < prices[min_index]:
                min_index = i
        return max_profit
            