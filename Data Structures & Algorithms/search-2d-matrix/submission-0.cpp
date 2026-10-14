class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {

        // Treat a matrix like a 1D array
        // Where each value in it goes like [0,1], [0,2], [0,3], etc
        // But then you can turn a 1D index into a 2D position
        // Then perform regular binary search as if its a 1D array
        
        int rows = matrix.size();
        int cols = matrix[0].size();

        // Example of how to turn 1D index into a 2D position
        // row = 6 / 4; // 1
        // col = 6 % 4; // 2

        // matrix[1][2] // 16

        int left = 0;
        int right = rows * cols - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            // How to convert a 1D index into a 2D position
            int row = mid / cols;
            int col = mid % cols;

            if (matrix[row][col] == target) {
                return true;
            }
            else if (matrix[row][col] < target) {
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }

        return false;
    }
};
