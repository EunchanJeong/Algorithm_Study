import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        char[][] arr = new char[n][m];

        for (int i = 0; i < n; i++) {
            arr[i] = br.readLine().toCharArray();
        }

        int check = Math.min(n, m);
        int answer = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                for (int k = 0; k < check; k++) {
                    if ((i + k) < n && (j + k) < m &&
                        arr[i][j] == arr[i][j + k] &&
                        arr[i][j] == arr[i + k][j] &&
                        arr[i][j] == arr[i + k][j + k]) {

                        answer = Math.max(answer, (k + 1) * (k + 1));
                    }
                }
            }
        }

        System.out.println(answer);
    }
}