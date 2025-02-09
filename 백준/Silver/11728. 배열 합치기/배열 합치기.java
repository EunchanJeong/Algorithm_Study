import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] A = new int[N];
        int[] B = new int[M];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            B[i] = Integer.parseInt(st.nextToken());
        }

        int a = 0, b = 0;
        while (a < N || b < M) {
            if (a == N) {
                sb.append(B[b++]).append(" ");
            } else if (b == M) {
                sb.append(A[a++]).append(" ");
            } else {
                if (A[a] < B[b]) {
                    sb.append(A[a++]).append(" ");
                } else {
                    sb.append(B[b++]).append(" ");
                }
            }
        }

        System.out.println(sb.toString().trim());
    }
}