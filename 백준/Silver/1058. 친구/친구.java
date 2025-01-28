import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static char[][] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        graph = new char[n][n];

        for (int i = 0; i < n; i++) {
            graph[i] = br.readLine().toCharArray();
        }

        int res = 0;
        for (int i = 0; i < n; i++) {
            res = Math.max(res, bfs(i));
        }

        System.out.println(res);
    }

    static int bfs(int v) {
        boolean[] visited = new boolean[n];
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{v, 0});
        visited[v] = true;
        int cnt = 0;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int a = current[0];
            int b = current[1];

            if (b >= 2) {
                continue;
            }

            for (int i = 0; i < n; i++) {
                if (!visited[i] && graph[a][i] == 'Y') {
                    cnt++;
                    visited[i] = true;
                    queue.add(new int[]{i, b + 1});
                }
            }
        }

        return cnt;
    }
}