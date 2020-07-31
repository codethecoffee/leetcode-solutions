# Link to problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

def maxProfit(prices):
    total_profit = 0
    length = len(prices)
    
    if length in {0, 1}:
        return total_profit
    
    for i in range(1, length):
        if prices[i-1] < prices[i]:
            # Buy at i-1 and sell at i
            total_profit += prices[i] - prices[i-1]
    
    return total_profit
