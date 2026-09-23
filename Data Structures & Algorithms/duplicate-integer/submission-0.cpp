class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> m1;

        for (int i = 0; i<nums.size(); i++){
            auto it = m1.find(nums[i]);
            if (it != m1.end()){
                return true;
            }
            m1.insert(nums[i]);
        }
        return false;
    }
};