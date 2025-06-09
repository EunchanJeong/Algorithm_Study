import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;
import java.util.LinkedList;

class Solution {
    public int solution(int n, int[][] edge) {
        int answer = 0;
        
        List<ArrayList<Integer>> graph = new ArrayList<>();
        
        for(int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }
        
        for(int[] e : edge) {
            int n1 = e[0];
            int n2 = e[1];
            
            graph.get(n1).add(n2);
            graph.get(n2).add(n1);
        }
        
        int[] result = new int[n+1];
        Arrays.fill(result, n+1);
        
        Deque<Integer> q = new LinkedList<>();
        q.add(1);
        result[1] = 0;
        
        while(!q.isEmpty()) {
            int node = q.poll();
            
            for(int next : graph.get(node)) {
                if(result[next] > result[node] + 1) {
                    result[next] = result[node] + 1;
                    q.offer(next);
                }
            }
        }
        
        Arrays.sort(result);
        int max = result[result.length-2];
        
        for(int i = result.length-2; i >= 0; i--) {
            if(result[i] != max) {
                break;
            }
            answer++;
        }
        return answer;
    }
}