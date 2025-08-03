import java.util.List;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Comparator;
import java.util.Arrays;

class Solution {
    public int solution(int N, int[][] road, int K) {
        List<List<int[]>> graph = new ArrayList<>();
        for(int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }
        
        for(int[] r : road) {
            int from = r[0];
            int to = r[1];
            int cost = r[2];
            
            graph.get(from).add(new int[]{to, cost});
            graph.get(to).add(new int[]{from, cost});
        }
        
        int[] dist = new int[N+1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        
        dist[1] = 0;
        
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        
        pq.offer(new int[]{1, 0});
        
        while(!pq.isEmpty()) {
            int[] current = pq.poll();
            int now = current[0];
            int cost = current[1];
            
            if(cost > dist[now]) {
                continue;
            }
            
            for(int[] next : graph.get(now)) {
                int neighbor = next[0];
                int nextCost = next[1];
                int total = cost + nextCost;
                
                if(total < dist[neighbor]) {
                    dist[neighbor] = total;
                    pq.offer(new int[]{neighbor, total});
                }
            }
        }
        
        int count = 0;
        for(int d : dist) {
            if(d <= K) {
                count++;
            }
        }
        
        return count;
    }
}