"""
You are given an array prices where prices[i] is
the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one 
stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not 
allowed because you must buy before you sell.

keeping a track of the lowest price and finding what day ahead has 
the greatest difference from that price
"""
import math 


def best_time(prices):
    max_profit = 0 
    lowest_price = math.inf
    
    for price in prices:
        lowest_price = min(lowest_price, price)
        max_profit = max(max_profit, price - lowest_price)
        
    return max_profit

if __name__ == "__main__":
    prices = [7,1,5,3,6,4] # 5
    prices = [7,6,4,3,1] # 0
    prices = [] # 0
    prices = [1] # 0
    prices = [2, 11, 5, 10] # 9
    print(best_time(prices))