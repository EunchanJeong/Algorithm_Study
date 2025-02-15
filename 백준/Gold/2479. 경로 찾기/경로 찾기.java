import java.util.*;
import java.io.*;

class Main {
    static int N, K;
    static List<String> codes = new ArrayList<>();
    static int[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        codes.add(""); 

        for (int i = 0; i < N; i++) {
            codes.add(br.readLine().trim());
        }

        st = new StringTokenizer(br.readLine());
        
        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());

        visited = new int[N + 1];

        System.out.println(bfs(start, end));
    }

    public static String bfs(int s, int e) {
        visited[s] = 1;

        Queue<Pair> q = new LinkedList<>();
        q.add(new Pair(s, String.valueOf(s)));

        while (!q.isEmpty()) {
            Pair current = q.poll();
            int num = current.index;
            String path = current.path;

            if (num == e) {
                return path;
            }

            for (int i = 1; i <= N; i++) {
                if (visited[i] == 1) continue;

                int diff = 0;
                for (int j = 0; j < K; j++) {
                    if (codes.get(num).charAt(j) != codes.get(i).charAt(j)) {
                        diff++;
                    }
                    if (diff > 1) break;
                }

                if (diff == 1) {
                    visited[i] = 1;
                    q.add(new Pair(i, path + " " + i));
                }
            }
        }

        return "-1";
    }
    
    static class Pair {
        int index;
        String path;

        Pair(int index, String path) {
            this.index = index;
            this.path = path;
        }
    }
}
