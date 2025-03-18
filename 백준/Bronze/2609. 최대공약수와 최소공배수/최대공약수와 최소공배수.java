import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        if(n < m) {
            int temp = n;
            n = m;
            m = temp;
        }
        
        int result1 = gcd(n, m);
        int result2 = (n * m) / result1;

        System.out.println(result1);
        System.out.println(result2);
    }


    static int gcd(int n, int m) {
        int r;
        while(m > 0) {
            r = n % m;
            n = m;
            m = r;
        }
        return n;
    }
}