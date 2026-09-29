class Solution {
public:
    bool isValid(string s) {
        stack<char> s1;
        for (char i: s){
            if (i == '{' || i == '(' || i == '['){
                s1.push(i);
            }
            else {
                if (s1.empty()) {
                    return false;
                }
                if (i == '}' && s1.top() == '{'){
                    s1.pop();
                }
                else if (i == ')' && s1.top() == '('){
                    s1.pop();
                }
                else if (i == ']' && s1.top() == '['){
                    s1.pop();
                }
                else {
                    return false;
                }
            }
        }
        if (s1.size() == 0){
            return true;
        }
        return false;
    }
};
