class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_stock=prices[0]
        current_profit=0
        max_profit=0
        for i in range(1,len(prices)):
            if prices[i]<buy_stock:
                buy_stock=prices[i]
            else:
                current_profit=prices[i]-buy_stock
                # buy_stock=prices[i]
            max_profit=max(max_profit,current_profit)
        return max_profit
