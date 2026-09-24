class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> m1;
        vector<vector<string>> v;

        // Make a key if it doesn't exist + append to value if key exists
        // Push back each value in map m1 in vector v
        // Return vector v

        for (const string& s : strs){
            // push_back for vector in value, already handles if key don't exist
            // key is already sorted so it finds it everytime if it exists
            // pushes original string
            string key = s;
            sort(key.begin(), key.end());  // make anagram key
            m1[key].push_back(s);
        }

        // Iterate through each member of m1 (aka need to iterate through each dict item)
        for (auto& [key, vec] : m1) {
            v.push_back(vec); // Push back whole vector
        }
        return v;
    }
};
