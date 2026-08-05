class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #subtraction with the highest return value
        # weeklyProfs = []
        # neetCashOut = 0


        # l,r = 0, len(prices) - 1
        # while l < r: 
        #     neetVal = prices[r] - prices[l]
        #     if prices[l] > prices[r]:
        #         l+=1
        #         neetVal = 0
        #     elif prices[l] < prices[r]:
        #         r-=1
        #     else:
        #         r-=1

        #     weeklyProfs.append(neetVal)

        # weeklyProfs.sort()
        # neetCashOut = weeklyProfs.pop()

        # return neetCashOut
        l,r = 0, 1
        maxNeet = 0
        currentPrice = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                currentPrice = prices[r] - prices[l]
            else:
                l = r  

            r+=1 #i dont get

            if currentPrice > maxNeet:
                maxNeet = currentPrice

        return maxNeet



                