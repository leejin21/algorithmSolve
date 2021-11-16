# Best Time to Buy and Sell Stock
# [파알인] 12. 주식을 사고팔기 가장 좋은 시점
import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        MIN = sys.maxsize
        PROFIT = -sys.maxsize

        for price in prices:
            MIN = min(price, MIN)
            PROFIT = max(PROFIT, price-MIN)
        return PROFIT