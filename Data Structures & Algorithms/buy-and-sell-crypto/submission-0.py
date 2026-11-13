class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = 0
        for i in range(1, len(prices)):
            if buy < prices[i]:
                result = prices[i] - buy
                if result > sell:
                    sell = result
            if buy > prices[i]:
                buy = prices[i] 
            # print(buy)
            # print(sell)
        return sell if sell != 0 else 0