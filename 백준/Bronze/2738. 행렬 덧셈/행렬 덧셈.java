import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());;

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] nums = new int[N][M];
        
        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            
            for(int j = 0; j < M; j++) {
                nums[i][j] =  Integer.parseInt(st.nextToken());
            }
        }

        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            
            for(int j = 0; j < M; j++) {
                nums[i][j] += Integer.parseInt(st.nextToken());
            }
        }

        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < M; j++) {
                sb.append(nums[i][j]).append(" ");
            }
            sb.append("\n");
        }

        System.out.println(sb.toString());
    }
}