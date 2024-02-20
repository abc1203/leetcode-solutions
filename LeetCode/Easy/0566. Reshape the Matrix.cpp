class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& mat, int r, int c) {
        int m = mat.size();
        int n = mat[0].size();

        if(m*n != r*c) return mat; // not legal

        vector<vector<int>> newMatrix;
        int curX = 0; int curY = 0;
        for(int i = 0; i < r; i++) {
            vector<int> newRow;
            for(int j = 0; j < c; j++) {
                newRow.push_back(mat[curX][curY]);
                curY++;
                if(curY == n) {
                    curX++;
                    curY = 0;
                }
            }
            newMatrix.push_back(newRow);
        }
        return newMatrix;
    }
};
