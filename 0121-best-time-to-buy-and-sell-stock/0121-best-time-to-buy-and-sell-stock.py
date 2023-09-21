class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # bestVal = 0

        # for i in range(0,len(prices)-1):
        #     for j in range(i+1, len(prices)):
        #         profit = prices[j] - prices[i]
        #         bestVal = max(bestVal,profit)
        # return bestVal

        bestVal = 0
        minVal = prices[0]
        for i in range(1,len(prices)):
            prof = prices[i] - minVal
            bestVal = max(bestVal,prof)
            minVal = min(minVal,prices[i])
        return bestVal