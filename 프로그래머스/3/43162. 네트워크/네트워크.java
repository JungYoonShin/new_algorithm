class Solution {
    void dfs(int v, int[][] computers, boolean[] visited) {
        visited[v] = true;
        for(int i=0; i<computers.length; i++) {
            if(i != v && computers[v][i] == 1 && !visited[i]) {
                dfs(i, computers, visited);
            }
        }
    }
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[computers.length];
    
        
        for(int i=0; i<computers.length; i++) {
            if(!visited[i]) {
                dfs(i, computers, visited);
                answer += 1;
            }
        }
        
        
        
        return answer;
    }
}