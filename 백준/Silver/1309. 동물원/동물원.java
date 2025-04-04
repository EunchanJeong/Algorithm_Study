import java.io.*;
import java.util.*;

public class Main {
    

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        if(N == 1) {
            System.out.println(3);
        }
        else {
            int[] dp = new int[N+1];

            dp[0] = 1;
            dp[1] = 3;
            dp[2] = 7;

            for(int i = 3; i < N+1; i++) {
                dp[i] = (dp[i-1] * 2 + dp[i-2]) % 9901;
            }

            System.out.println(dp[N]);
        }
    }
}