import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int M;
    static int K;
    static int[][] graph;
    static boolean[][] visited;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        List<int[]> g = new ArrayList<>();

        graph = new int[N][M];
        visited = new boolean[N][M];
        
        for(int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());

            int r = Integer.parseInt(st.nextToken()) - 1;
            int c = Integer.parseInt(st.nextToken()) - 1;

            graph[r][c] = 1;
            g.add(new int[] {r, c});
        }

        int result = 0;
        for(int[] point : g) {
            int r = point[0];
            int c = point[1];

            if(!visited[r][c]) {
                int tmp = bfs(point[0], point[1]);

                if(result < tmp) {
                    result = tmp;
                }
            }
        }

        System.out.println(result);
    }

    static int bfs(int a, int b) {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[] {a, b});
        visited[a][b] = true;
        
        int[] dx = new int[] {-1, 0, 1, 0};
        int[] dy = new int[] {0, 1, 0, -1};
        
        int count = 1;
        while(!q.isEmpty()) {
            int[] p = q.poll();

            for(int i = 0; i < 4; i++) {
                int nx = p[0] + dx[i];
                int ny = p[1] + dy[i];

                if(nx >= 0 && nx < N && ny >= 0 && ny < M) {
                    if(!visited[nx][ny] && graph[nx][ny] == 1) {
                        count++;
                        q.add(new int[] {nx, ny});
                        visited[nx][ny] = true;
                    }
                }
            }
        }
        return count;
    }
}