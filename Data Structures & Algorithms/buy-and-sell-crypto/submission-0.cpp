class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxP = 0;
        int minBuy = prices[0];

        for (int sell = 0; sell < prices.size(); sell++){
            maxP = max(maxP, prices[sell] - minBuy);
            minBuy = min(minBuy, prices[sell]);
        }
        return maxP;
    }
};
