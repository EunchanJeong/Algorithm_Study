import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long N = Long.parseLong(br.readLine());

        long result = 1;
        for(long i = N; i > 0; i--) {
            result *= i;
        }

        System.out.println(result);
    }
}