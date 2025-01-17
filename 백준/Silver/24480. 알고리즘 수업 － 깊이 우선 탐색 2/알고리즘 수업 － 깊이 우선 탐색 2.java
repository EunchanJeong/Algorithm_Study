import java.io.*;
import java.util.*;

public class Main {
    static int N, M, R;
    static List<List<Integer>> graph = new ArrayList<>();
    static boolean[] visited;
    static int[] result;
    static int count = 1;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());

        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }
        visited = new boolean[N + 1];
        result = new int[N + 1];

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        for (List<Integer> g : graph) {
            g.sort(Collections.reverseOrder());
        }

        dfs(R);

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= N; i++) {
            sb.append(result[i]).append("\n");
        }
        System.out.print(sb);
    }

    static void dfs(int v) {
        visited[v] = true;
        result[v] = count;

        for (int n : graph.get(v)) {
            if (!visited[n]) {
                count++;
                dfs(n);
            }
        }
    }
}