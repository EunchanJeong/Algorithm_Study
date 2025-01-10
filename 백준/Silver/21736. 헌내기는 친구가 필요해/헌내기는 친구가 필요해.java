import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static char[][] graph;
    static boolean[][] visited;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};

    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        graph = new char[N][M];
        visited = new boolean[N][M];

        int startX = 0;
        int startY = 0;
        
        for(int i = 0; i < N; i++) {
            String row = br.readLine();

            for(int j = 0; j < M; j++) {
                graph[i][j] = row.charAt(j);

                if(graph[i][j] == 'I') {
                    startX = i;
                    startY = j;
                }
            }
        }

        int result = bfs(startX, startY);

        if(result == 0) {
            System.out.println("TT");
        }
        else {
            System.out.println(result);
        }

        
    }

    static int bfs(int x, int y) {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{x, y});
        visited[x][y] = true;

        int count = 0;
        while(!q.isEmpty()) {
            int[] current = q.poll();
            int curX = current[0];
            int curY = current[1];

            for(int i = 0; i < 4; i++) {
                int nx = curX + dx[i];
                int ny = curY + dy[i];

                if(nx >= 0 && nx < N && ny >= 0 && ny < M) {
                    if(!visited[nx][ny]) {
                        if(graph[nx][ny] == 'P') {
                            count++;
                            q.add(new int[]{nx, ny});
                            visited[nx][ny] = true;
                        }
                        else if(graph[nx][ny] == 'O') {
                            q.add(new int[]{nx, ny});
                            visited[nx][ny] = true;
                        }
                    }
                }
            }
        }

        return count;
    }
}