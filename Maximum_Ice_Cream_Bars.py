class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n=0
        costs.sort()
        for i in range(len(costs)):
            coins=coins-costs[i]
            if coins < 0:
                break
            n=n+1
                
        return n
