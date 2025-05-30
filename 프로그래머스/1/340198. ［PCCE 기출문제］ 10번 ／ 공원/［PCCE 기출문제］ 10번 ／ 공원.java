import java.util.*;
class Solution {
    public int solution(int[] mats, String[][] park) {
        ArrayList<Integer> answer = new ArrayList<>(); 
        
        int row = park.length;
        int col = park[0].length;

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {

                if (park[i][j].equals("-1")) {

                    for (int k = 0; k < mats.length; k++) {
                        int mat = mats[k];
                        boolean flag = true;

                        for (int n = 0; n < mat; n++) {
                            for (int p = 0; p < mat; p++) {
                                if (i + n < row && j + p < col) {
                                    if (!park[i + n][j + p].equals("-1")) {
                                        flag = false;
                                        break;
                                    }
                                } else {
                                    flag = false;
                                    break;
                                }
                            }
                            if (!flag) break;
                        }

                        if (flag) {
                            answer.add(mat);
                        }
                    }

                }
            }
        }
        if (answer.isEmpty()) return -1;
        return Collections.max(answer);
    }
}