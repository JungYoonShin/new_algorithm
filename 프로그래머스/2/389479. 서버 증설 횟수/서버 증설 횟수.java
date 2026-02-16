import java.util.*;
class Solution {
    public int solution(int[] players, int m, int k) {
        int answer = 0;
        int[] server = new int[25];
        
        for(int i=0; i<players.length; i++) {
            int need = players[i] / m;
            if(need > server[i]) {
                int add = need - server[i];
                answer += add;
                for(int j=0; j<k; j++) {
                    if(i+j<=23) {
                        server[i+j] += add;
                    }
                }
            }
        }
        
        System.out.println(answer);
        return answer;
    }
}