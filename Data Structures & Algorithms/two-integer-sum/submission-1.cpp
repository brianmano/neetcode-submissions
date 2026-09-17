class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m; // Hashmap

        for (int i = 0; i < nums.size(); i++){
            int temp = target - nums[i];
            auto it = m.find(temp); // .find looks for key ONLY
            if (it != m.end()){ // makes sure it doesn't hand you the end cause it does that. m.end() is the exact same idea, but for iterators instead of indices. It marks "one past the last element" — a boundary marker, not real data.
                return {it->second, i};
            }
            m[nums[i]] = i; // Store nums value in key, store indices in value, since .find only looks for key, which will have the value stored
        }
        return {}; // Didn't find anything
    }
};
