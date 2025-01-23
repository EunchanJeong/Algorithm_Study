import java.io.*;
import java.util.*;

public class Main {
    static int[][] graph;
    static int N;
    static int[][] directions = {
        {-2, -1}, {-2, 1}, {0, -2}, {0, 2}, {2, -1}, {2, 1}
    };

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int sr = Integer.parseInt(st.nextToken());
        int sc = Integer.parseInt(st.nextToken());
        int er = Integer.parseInt(st.nextToken());
        int ec = Integer.parseInt(st.nextToken());

        graph = new int[N][N];
        for (int i = 0; i < N; i++) {
            Arrays.fill(graph[i], -1);
        }

        bfs(sr, sc);

        System.out.println(graph[er][ec]);
    }

    private static void bfs(int r, int c) {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[] {r, c});
        graph[r][c] = 0;

        while (!q.isEmpty()) {
            int[] current = q.poll();
            int cr = current[0];
            int cc = current[1];

            for (int[] dir : directions) {
                int nr = cr + dir[0];
                int nc = cc + dir[1];

                if (nr >= 0 && nr < N && nc >= 0 && nc < N && graph[nr][nc] == -1) {
                    q.add(new int[] {nr, nc});
                    graph[nr][nc] = graph[cr][cc] + 1;
                }
            }
        }
    }
}
