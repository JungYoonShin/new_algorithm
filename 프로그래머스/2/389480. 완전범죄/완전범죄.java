import java.util.Arrays;

class Solution {
	public int solution(int[][] info, int n, int m) {
		int answer = n;
		int[][] dp = new int[info.length][m];
        
        
        for(int i=0; i<info.length; i++) {
            Arrays.fill(dp[i], n);
        }
        
        dp[0][0] = info[0][0];
        if(info[0][1] < m) {
            dp[0][info[0][1]] = 0;
        }
        
		for (int i = 1; i < info.length; i++) {
			int a = info[i][0];
			int b = info[i][1];

			for (int j = 0; j < m; j++) {
				//A도둑이 물건을 훔치는 경우
				dp[i][j] = Math.min(dp[i][j], dp[i-1][j] + a );

				//i번째 물건을 B가 훔칠 수 있을 경우
				if(j + b < m) {
					dp[i][j+b] = Math.min(dp[i][j+b], dp[i-1][j]);
				}
			}
		}
        for (int i = 0; i < m; i++) {
			if(answer > dp[info.length - 1][i]) {
				answer = dp[info.length - 1][i];
			}
		}

		return answer >= n ? -1 : answer;
	}

}