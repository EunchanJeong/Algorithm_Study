import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] A = new int[N][M];

        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            
            for(int j = 0; j < M; j++) {
                A[i][j] = Integer.parseInt(st.nextToken());;
            }
        }
        
        int[][] DP = new int[N+1][M+1];

        for(int i = 1; i < N+1; i++) {
            for(int j = 1; j < M+1; j++) {
                DP[i][j] = DP[i][j-1] + DP[i-1][j] - DP[i-1][j-1] + A[i-1][j-1];
            }
        }

        int K = Integer.parseInt(br.readLine());

        for(int t = 0; t < K; t++) {
            st = new StringTokenizer(br.readLine());
            
            int i = Integer.parseInt(st.nextToken());
            int j = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            System.out.println(DP[x][y] - DP[x][j-1] - DP[i-1][y] + DP[i-1][j-1]);
        }     
    }
}