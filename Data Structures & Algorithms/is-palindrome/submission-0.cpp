class Solution {
public:
    bool isPalindrome(string s) {

        vector<char> v1;

        for (int m = 0; m<s.size(); m++){
            if (isalnum(s[m])){
                v1.push_back(tolower(s[m]));
            }
        }

        int i = 0;
        int j = v1.size() - 1;

        while (i<=j){
            if (v1[i] != v1[j]){
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
};
