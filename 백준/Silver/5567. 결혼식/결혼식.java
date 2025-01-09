import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        
        List<List<Integer>> graph = new ArrayList<>();
        for(int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for(int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        int[] visited = new int[n+1];
        Queue<Integer> q = new LinkedList<>();
        q.add(1);
        visited[1] = 1;

        while(!q.isEmpty()) {
            int next = q.poll();

            for(int t : graph.get(next)) {
                if(visited[t] == 0) {
                    q.add(t);
                    visited[t] = visited[next] + 1;
                }
            }
        }

        int count = 0;
        for(int i = 2; i <= n; i++) {
            if(visited[i] >= 1 && visited[i] <= 3) {
                count++;
            }
        }
        System.out.println(count);
    }
}