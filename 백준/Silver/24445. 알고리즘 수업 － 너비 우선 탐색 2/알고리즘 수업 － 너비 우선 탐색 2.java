import java.io.*;
import java.util.*;

public class Main {
    static int[] visited;
    static ArrayList<Integer>[] graph;
    static int N;
    static int M;
    static int R;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N+1];
        for (int i = 1; i <= N; i++) {
            graph[i] = new ArrayList<>();
        }

        for(int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph[a].add(b);
            graph[b].add(a);
        }

        for(int i = 1; i <= N; i++) {
            Collections.sort(graph[i], Collections.reverseOrder());
        }

        visited = new int[N+1];
        bfs(R);

        for(int i = 1; i <= N; i++) {
            System.out.println(visited[i]);
        }
    }

    private static void bfs(int start) {
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        visited[start] = 1;
        int count = 1;

        while(!q.isEmpty()) {
            int v = q.poll();

            for(int n : graph[v]) {
                if(visited[n] == 0) {
                    q.add(n);
                    count++;
                    visited[n] = count;
                }
            }
        }
        
    }
}