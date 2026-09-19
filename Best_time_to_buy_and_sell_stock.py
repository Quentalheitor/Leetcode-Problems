class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        buy_day = 0
        sell_day = 1
        profit = 0
        if len(prices) <= 1:
            return profit
        while buy_day < sell_day:
            new_profit = prices[sell_day] - prices[buy_day]
            if profit <= new_profit:
                profit = new_profit
            if prices[buy_day] > prices[sell_day]:
                buy_day = sell_day
            if sell_day != len(prices) -1:
                sell_day += 1
            else:
                return profit



solucao = Solution
print(solucao.maxProfit(solucao,prices=[7,6,4,3,1])) 