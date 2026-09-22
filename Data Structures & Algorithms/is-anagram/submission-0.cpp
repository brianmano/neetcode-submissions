class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> map1;
        unordered_map<char, int> map2;

        // If they have different lengths, impossible for anagram
        for( int i=0; i<s.size(); i++ ){
            //If the key exists → it points to that element
            //If the key does NOT exist → it == map1.end()
            auto it = map1.find(s[i]);
            // If the key hasn't reached the end, it was found
            if (it != map1.end()){
                map1[s[i]]++;
            }
            else{
                map1[s[i]] = 1;
            }
        }

        for( int i=0; i<t.size(); i++ ){
            auto it = map2.find(t[i]);
            if (it != map2.end()){
                map2[t[i]]++;
            }
            else {
                map2[t[i]] = 1;
            }
            
        }

        if (map1 == map2){
            return true;
        }
        return false;
    }
};
