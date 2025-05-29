class Solution {
    public int solution(int n, int w, int num) {
        int row = (num - 1) / w;
        int indexInRow = (num - 1) % w;
        int col = (row % 2 == 0) ? indexInRow : w - 1 - indexInRow;
        
        int count = 0;
        for (int r = row + 1; r <= (n - 1) / w; r++) {
            int topIndex = r * w + (r % 2 == 0 ? col : w - 1 - col);
            if (topIndex < n) {
                count++;
            }
        }

        return count + 1;
    }
}
