public class Solution {
    public bool IsAnagram(string s, string t) {
        Dictionary<char, int> dictionary = new Dictionary<char, int>();
        
        if (s.Length != t.Length){
            return false;
        }
        for (int i = 0; i < s.Length;i++){
            char temp = s[i];
            if (dictionary.ContainsKey(temp)){
                dictionary[temp]++;
            }
            else {
                dictionary[temp] = 1;
            }
        }

        for (int i = 0; i < t.Length; i++){
            char temp = t[i];
            if (!dictionary.ContainsKey(temp) || dictionary[temp] == 0){
                return false;
            }
            else {
                dictionary[temp]--;
            }
        }
        return true;
        
    }
}
