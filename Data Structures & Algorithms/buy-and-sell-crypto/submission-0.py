class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # keep track of lowest price
        # use max to determine best profit the difference in current price and lowest
        lowest = prices[0]
        result = 0
        for price in prices:
            if price < lowest:
                lowest = price
            result = max(result, price - lowest)

        return result