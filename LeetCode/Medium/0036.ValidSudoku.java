class Solution {
    public boolean checkValid(char[] check) {
        for(int i = 0; i < 9; ++i) {
            for(int j = i+1; j < 9; ++j) {
                if(check[i] == check[j] && check[i] != '.') {
                    return false;
                }
            }
        }
        return true;
    }


    public boolean isValidSudoku(char[][] board) {
        char[] check = new char[9];

        // check all rows
        for(int row = 0; row < 9; ++row) {
            for(int i = 0; i < 9; ++i) {
                check[i] = board[row][i];
            }
            if(!checkValid(check)) return false;
        }

        // check all cols
        for(int col = 0; col < 9; ++col) {
            for(int j = 0; j < 9; ++j) {
                check[j] = board[j][col];
            }
            if(!checkValid(check)) return false;
        }

        // check all subsquares
        for(int startRow = 0; startRow < 9; startRow+=3) {
            for(int startCol = 0; startCol < 9; startCol+=3) {
                // check individual subsquare
                int ind = 0;
                for(int i = startRow; i < startRow+3; ++i) {
                    for(int j = startCol; j < startCol+3; ++j) {
                        check[ind] = board[i][j];
                        ++ind;
                    }
                }
                if(!checkValid(check)) return false;
            }
        }

        return true;
    }
}
