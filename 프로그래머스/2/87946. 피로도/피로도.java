class Solution {
    static int answer = 0;
    static boolean[] visited;
    
    public int solution(int k, int[][] dungeons) {
        
        visited = new boolean[dungeons.length];
        
        dfs(0, k, dungeons);
        return answer;
    }
    
    private void dfs(int count, int fatigue, int[][] dungeons) {
        for(int i = 0; i < dungeons.length; i++) {
            if(visited[i] || dungeons[i][0] > fatigue) {
                continue;
            }
            else {
                visited[i] = true;
                dfs(count+1, fatigue - dungeons[i][1], dungeons);
                visited[i] = false;
            }
        }
        answer = Math.max(answer, count);
    }
}