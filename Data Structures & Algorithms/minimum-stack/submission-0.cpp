class MinStack {
private:
    // (value, minimum_at_that_point)
    stack<pair<int, int>> s;

public:
    MinStack() {}

    void push(int val) {
        if (s.empty()) {
            // Pushes val and setting current min as the only value
            s.push({val, val});
        } else {
            // Updates current min if val is smaller
            int currentMin = min(val, s.top().second);
            s.push({val, currentMin});
        }
    }
    // Pops top value normally
    void pop() {
        s.pop();
    }

    int top() {
    // Stores top value stored in first
        return s.top().first;
    }
    // Returns current min stored in second
    int getMin() {
        return s.top().second;
    }
};
