# You are given an array prices where prices[i] is the price of a given
# stock on the ith day.
# Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def max_profit(prices: list[int]) -> int:
    right = 1
    left = 0
    result = 0

    while right < len(prices):
        if prices[left] < prices[right]:
            gain = prices[right] - prices[left]

            result = max(result, gain)
        else:
            left = right

        right = right + 1
    
    return result
