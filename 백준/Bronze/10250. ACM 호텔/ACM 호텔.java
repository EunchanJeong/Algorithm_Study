import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        
        StringTokenizer st;
        for(int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine());

            int H = Integer.parseInt(st.nextToken());
            int W = Integer.parseInt(st.nextToken());
            int N = Integer.parseInt(st.nextToken());

            int x = (N/H) + 1;
            int y = N % H;
            if(N%H == 0) {
                x = N / H;
                y = H;
            }
            System.out.println(y * 100 + x);
        }
    }
}