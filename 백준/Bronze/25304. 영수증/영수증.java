import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        long X = Long.parseLong(br.readLine());
        long N = Long.parseLong(br.readLine());

        StringTokenizer st;
        long result = 0;
        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());

            long a = Long.parseLong(st.nextToken());
            long b = Long.parseLong(st.nextToken());

            result += a*b;
        }

        if(result == X) {
            System.out.println("Yes");
        }
        else {
            System.out.println("No");
        }
    }
}