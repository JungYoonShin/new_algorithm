class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        
        boolean[] visited = new boolean[n];
        for(int i=0; i<n; i++) {
            if(!visited[i]) {
                dfs(i, visited, computers, n);
                answer += 1;
            }
                    }
        
        return answer;
    }
    
    public void dfs(int start, boolean[] visited, int[][] computers, int n) {
    visited[start] = true;

    for (int i = 0; i < n; i++) {
        if(i!=start && computers[start][i] == 1 && visited[i] != true) {
            dfs(i, visited, computers, n);
        }
    }
    }
}

