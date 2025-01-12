import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[][] graph;
    static boolean[][] visited;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        graph = new int[N][N];
        visited = new boolean[N][N];
        for(int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for(int i = 0; i < N; i++) {
            bfs(i);
        }

       StringBuilder sb = new StringBuilder();
       for(int i = 0; i < N; i++) {
           for(int j = 0; j < N; j++) {
               sb.append(visited[i][j] ? 1 : 0).append(" ");
           }
           sb.append("\n");
        }

        System.out.println(sb.toString());
    
    }

    static void bfs(int start) {
        Queue<Integer> q = new LinkedList<>();
        q.add(start);

        while(!q.isEmpty()) {
            int a = q.poll();

            for(int i = 0; i < N; i++) {
                if(!visited[start][i]) {
                    if(graph[a][i] == 1) {
                        q.add(i);
                        visited[start][i] = true;
                    }
                }
            }
        }
    }
}