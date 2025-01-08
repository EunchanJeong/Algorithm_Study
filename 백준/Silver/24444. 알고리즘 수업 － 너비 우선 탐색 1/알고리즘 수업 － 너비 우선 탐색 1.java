import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());

        List<List<Integer>> graph = new ArrayList<>();
        for(int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }

        for(int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        for(List<Integer> g : graph) {
            Collections.sort(g);
        }

        int[] visited = new int[N+1];

        Queue<Integer> q = new LinkedList<>();
        q.add(R);
        visited[R] = 1;

        int count = 2;
        while(!q.isEmpty()) {
            int n = q.poll();

            for(int t : graph.get(n)) {
                if(visited[t] == 0) {
                    q.add(t);
                    visited[t] = count++;
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for(int i = 1; i <= N; i++) {
            sb.append(visited[i]).append("\n");
        }
        System.out.println(sb.toString());
        
    }
}