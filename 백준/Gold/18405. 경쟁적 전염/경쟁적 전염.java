import java.util.*;
import java.io.*;

class Dot {
    int x;
    int y;
    int n;

    Dot(int x, int y, int n) {
        this.x = x;
        this.y = y;
        this.n = n;
    }

    int getX() {
        return x;
    }
    int getY() {
        return y;
    }
    int getN() {
        return n;
    }
}

class Main {
    static int N;
    static int K;
    static int S;
    static int X;
    static int Y;
    
    static int[][] graph;
    static int[][] visited;


    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        graph = new int[N][N];
        visited = new int[N][N];
        
        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            
            for(int j = 0; j < N; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        st = new StringTokenizer(br.readLine());
        
        S = Integer.parseInt(st.nextToken());
        X = Integer.parseInt(st.nextToken());
        Y = Integer.parseInt(st.nextToken());

        bfs(graph);
        System.out.println(graph[X-1][Y-1]);
       
    }

    private static Queue<Dot> searchDot(int[][] graph) {
        Queue<Dot> q = new LinkedList<>();

        for(int n = 1; n < K+1; n++) {
            for(int i = 0; i < N; i++) {
                for(int j = 0; j < N; j++) {
                    if(graph[i][j] == n) {
                        q.add(new Dot(i, j, n));
                        visited[i][j] = 1;
                    }
                }
            }
        }

        return q;
    }
    private static void bfs(int[][] graph) {
        Queue<Dot> q = searchDot(graph);

        int[] dx = {-1, 0, 1, 0};
        int[] dy = {0, 1, 0, -1};
        boolean stop = false;

        while(!q.isEmpty()) {
            Dot dot = q.poll();

            int x = dot.getX();
            int y = dot.getY();
            int n = dot.getN();

            for(int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if(nx >= 0 && nx < N && ny >= 0 && ny < N) {
                    if(graph[nx][ny] == 0 && visited[nx][ny] == 0) {
                        graph[nx][ny] = n;
                        q.add(new Dot(nx, ny, n));

                        if(visited[x][y] + 1 > S) {
                            stop = true;
                            break;
                        }
                            
                        visited[nx][ny] = visited[x][y] + 1;
                    }
                }
            }

            if(stop) {
                break;
            }
        }
    }
}