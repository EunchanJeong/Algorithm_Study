import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine().trim();
        int N = Integer.parseInt(br.readLine());

        System.out.println(str.substring(N-1, N));
    }
}