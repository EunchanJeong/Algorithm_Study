import java.util.*;
import java.io.*;

class Dot {
    int x;
    int y;

    public Dot(int x, int y) {
        super();
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }
}
class Main {
    static int[][] arr;
    static int[][] visited;
    static int N;
    static int M;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        arr = new int[M][N];
        visited = new int[M][N];
        
        for(int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            
            for(int j = 0; j < N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());  
            }
        }

        int count = 0;
        for(int i = 0; i < M; i++) {
            for(int j = 0; j < N; j++) {

                if(arr[i][j] == 1 && visited[i][j] == 0) {
                    bfs(i, j);
                    count++;
                }  
            }
        }

        System.out.println(count);
    }

    private static void bfs(int a, int b) {
        int[] dx = {0, 1, 1, 1, 0, -1, -1, -1};
        int[] dy = {1, 1, 0, -1, -1, -1, 0, 1};

        Queue<Dot> q = new LinkedList<>();

        q.add(new Dot(a, b));
        visited[a][b] = 1;

        while(!q.isEmpty()) {
            Dot dot = q.poll();
            int x = dot.getX();
            int y = dot.getY();

            for(int i = 0; i < 8; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if(nx >= 0 && nx < M && ny >= 0 && ny < N && arr[nx][ny] == 1 && visited[nx][ny] == 0) {
                    q.add(new Dot(nx, ny));
                    visited[nx][ny] = 1;
                }
            }
        } 
    }
}